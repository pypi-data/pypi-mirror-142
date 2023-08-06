from ipywidgets import widgets, interact, Layout
from rwth_nb.misc.submission import Submission
import rwth_nb.plots.colors as rwthcolors

rwth_colors = rwthcolors.rwth_colors

import datetime
import json
import os
import hashlib
import platform
import subprocess

import pandas as pd

import matplotlib.pyplot as plt

# Internationalization
supported_languages = ['en', 'de']

feedback_scale_options_en = ['Strongly agree', 'Agree', 'Neutral', 'Disagree', 'Strongly disagree']

feedback_scale_options_de = ['Stimme voll zu', 'Ich stimme zu', 'Keine Meinung', 'Ich stimme nicht zu',
                             'Ich stimme gar nicht zu']

feedback_text_en = {"your-feedback": "Your Feedback ...",
                    "send": "Submit",
                    "confirm_send": "Confirm submission.",
                    "sent": "Feedback was submitted. Thank You!",
                    "required": "Required field",
                    "empty": "Please fill required fields before submitting.",
                    "mailfailure": "The mail containing your feedback could not be sent. Your feedback was saved locally."
                    }

feedback_text_de = {"your-feedback": "Feedback ...",
                    "send": "Abschicken",
                    "confirm_send": "Abschicken bestätigen.",
                    "sent": "Das Feedback wurde abgeschickt. Vielen Dank!",
                    "required": "Pflichtfeld",
                    "empty": "Bitte ein Feedback eingeben, das abgesendet werden kann.",
                    "mailfailure": "Die Mail mit dem Feedback konnte nicht versendet werden. Das Feedback wurde lokal abgespeichert."}


def get_notebook_name():
    try:
        # import necessary packages (see https://github.com/jupyter/notebook/issues/1000)
        # importing inside function because those libraries should only be included if they are realy needed
        import json
        import re
        import ipykernel
        import requests
        import os

        from requests.compat import urljoin
        from notebook.notebookapp import list_running_servers

        # now determine calling notebook name
        kernel_id = re.search('kernel-(.*).json',
                              ipykernel.connect.get_connection_file()).group(1)
        servers = list_running_servers()
        for ss in servers:
            response = requests.get(urljoin(ss['url'], 'api/sessions'),
                                    params={'token': ss.get('token', '')})
            for nn in json.loads(response.text):
                if nn['kernel']['id'] == kernel_id:
                    relative_path = nn['notebook']['path']
                    return os.path.splitext(os.path.split(os.path.join(ss['notebook_dir'], relative_path))[1])[0]
    except:
        return 'tmp'


class RWTHFeedbackBase:
    is_submit_confirmed = is_submitted = False

    def __init__(self, feedback_name, questions, lang):
        self.feedback_name = feedback_name
        self.questions = questions

        if lang not in supported_languages:
            raise Exception('Language \'{}\' not supported. Supported languages are: {}'.format(lang, supported_languages))

        user_name = os.environ.get('JUPYTERHUB_USER',
                                   os.environ.get('LOGNAME', os.environ.get('USER', os.environ.get('USERNAME', 'TMP'))))
        self.hashed_username = hashlib.sha256(str.encode(user_name)).hexdigest()

        # Select language
        self.feedback_scale_options = globals()['feedback_scale_options_' + lang]
        self.feedback_text = globals()['feedback_text_' + lang]

        # Default arguments for toggle_button and textarea
        self.toggle_args = {"options": self.feedback_scale_options,
                            "index": 2, "description": "", "disabled": False,
                            "style": {'button_color': rwth_colors['rwth:green-50']}, "tooltips": []}
        self.textarea_args = {"value": "", "placeholder": self.feedback_text['your-feedback'],
                              "description": "", "disabled": False}

        # self.widgets_container:
        #   dict containing to each id key as defined in q a widget
        #   i.e. {'likes': widgets.Textarea, ...}
        self.widgets_container = {}

        # self.widgets_VBoxes:
        #   list containing vertical boxes with labels and according widgets
        #   used for ui design
        self.widgets_VBoxes = []

        # self.widgets_required_entries
        #   list containing all widgets that require non empty entries
        self.widgets_required_entries = []

        self.entry = {}
        self.entries = []

        # set up UI
        self.setup_ui()

    def setup_ui(self):
        """
        Set up user interface according to given questions
        """
        for question in self.questions:
            if question['type'] == 'free-text':
                # Free text
                widget_label = widgets.HTML(value="<b>{}</b>".format(question['label']))
                widget_value = widgets.Textarea(**self.textarea_args)

            elif question['type'] == 'free-text-required':
                # Required Free text
                widget_label = widgets.HTML(value="<b>{}</b>*".format(question['label']))
                widget_value = widgets.Textarea(**self.textarea_args)
                self.widgets_required_entries.append(widget_value)

            elif question['type'] == 'scale':
                # Toggle Buttons
                widget_label = widgets.HTML(value="<b>{}</b>".format(question['label']))
                widget_value = widgets.ToggleButtons(**self.toggle_args)

            self.widgets_VBoxes.append(widgets.VBox([widget_label, widget_value]))
            self.widgets_container[question['id']] = widget_value

        # Button
        self.btn_submit = widgets.Button(description=self.feedback_text['send'], disabled=False,
                                         style={'button_color': rwth_colors['rwth:green-50'], 'margin': '10px'},
                                         icon='',
                                         layout=Layout(margin='20px 0 0 0', width='auto'))

        # widget for displaying required field annotation
        self.widget_required_field = widgets.HTML(value="<i>*{}</i>".format(self.feedback_text['required']))

        self.output = widgets.Output()

        self.btn_submit.on_click(self.on_btn_submit_clicked)

        # Display widgets
        if len(self.widgets_required_entries):
            display(widgets.VBox(self.widgets_VBoxes), self.widget_required_field,
                    self.btn_submit, self.output);
        else:
            display(widgets.VBox(self.widgets_VBoxes), self.btn_submit, self.output);

        self.update_ui_state()

    def on_btn_submit_clicked(self, _):
        """
        Submit button onClick method

        Sets current json entry
        Calls send_mail method
        Sets status of all entries to submitted if mail was sent successful.
        Otherwise entries are locally saved.
        """
        # set up json entries
        self.entry['name'] = self.feedback_name
        self.entry['date'] = "{}".format(datetime.datetime.now())
        self.entry['userhash'] = self.hashed_username
        self.entry['answer'] = {key: w.value for key, w in self.widgets_container.items()}
        self.entry['status'] = 'saved_locally' if self.submission_type == 'json' else 'submitted'
        self.entry['types'] = {key: [q['id'] for q in self.questions if q['type'] in (key, f'{key}-required')]
                               for key in ('free-text', 'scale')}

        # check if required entries are empty
        for w in self.widgets_required_entries:
            if not w.value.strip():
                self.output.clear_output()
                with self.output:
                    print(self.feedback_text['empty'])
                    return

        # confirm submission if not happened already
        if not self.is_submit_confirmed:
            self.btn_submit.description = self.feedback_text['confirm_send']
            self.btn_submit.layout.width = 'auto'
            self.is_submit_confirmed = True
            return

        # submit
        self.submit()

        # update ui
        self.update_ui_state()

    def check_submission_status(self):
        for entry in self.entries:
            if self.feedback_name == entry['name']:
                return entry['status']
        return 'idle'

    def update_ui_state(self):
        """
        Updates UI state according to feedback submission status.

        Calls either:
        ui_state_idle, ui_state_saved_locally or ui_state_submitted
        according to returned string from check_submission_status
        """
        self.load_entries()

        self.status = self.check_submission_status()

        getattr(self, 'ui_state_' + self.status)()

    def ui_state_idle(self):
        """
        Sets UI state to idle
        # all free-text and scales are left untouched
        # submit button enabled
        """
        pass

    def ui_state_saved_locally(self):
        """
        Sets UI state to saved_locally

        All free-text and scales filled with and set to locally saved answers
        Submit button is enabled
        """
        # get existing entry
        for entry in self.entries:
            if self.feedback_name == entry['name']:
                self.entry = entry

        # set widgets values to locally saved answers
        try:
            for key, w in self.widgets_container.items():
                w.value = self.entry['answer'][key]
        except KeyError:
            self.output.clear_output()
            with self.output:
                print('Something went wrong! Contact notebook provider.')

    def ui_state_submitted(self):
        """
        Sets UI state to submitted

        All widgets are filled with locally saved answers
        All widgets and submit button are disabled
        """
        # call saved_locally state for filling widgets with saved answers
        self.output.clear_output()

        self.ui_state_saved_locally()

        # disable all widgets
        for w in self.widgets_container.values():
            w.disabled = True

        # disable button and change description
        self.btn_submit.disabled = True
        self.btn_submit.description = self.feedback_text['sent']


class RWTHFeedbackJupyter(RWTHFeedbackBase):
    """ RWTH Feedback submission with RWTHJupyters submission service

    Parameters
    ----------
    feedback_name: str
        the feedbacks name
    questions: dict
        feedback options to be filled out
    lang: str, optional
        feedback language, scales are shown in that language
    realm: str, optional
        jupyter submission realm in which the feedback should be stored, is set automatically if None
    """

    def __init__(self, feedback_name, questions, lang='en', realm=None):
        self.realm = realm

        profile = os.environ.get('JUPYTERHUB_PROFILE')
        self.realm = f'feedback_{profile}' if self.realm is None else self.realm
        self.sub = Submission(self.realm)

        super().__init__(feedback_name, questions, lang)

        self.submission_type = 'jupyter'

    def load_entries(self):
        self.entries = [submission['data'] for submission in self.sub.get()
                        if type(submission['data']) is dict and submission['data'].get('name') is not None]

    def submit(self):
        # submit to jupyter submission service
        self.sub.submit(self.entry)

        self.is_submitted = True


class RWTHFeedbackMail(RWTHFeedbackBase):
    """ RWTH Feedback submission with mail

    Parameters
    ----------
    feedback_name: str
        the feedbacks name
    questions: dict
        feedback options to be filled out
    lang: str, optional
        feedback language, scales are shown in that language
    feedback_path: str, optional
        path in which a feedback json file should be stored
    mail_to: str, optional
        mail adress to which the feedback should be sent when submitted
    mail_from: str, optional
        mail adress from which the feedback should be sent when submitted
    mail_subject: str, optional
        subject of the mail
    mail_smtp_host: str, optional
        smtp host
    """

    def __init__(self, feedback_name, questions, lang='en', feedback_path='feedback.json', mail_to=None,
                 mail_from='feedback@jupyter.rwth-aachen.de', mail_subject=None,
                 mail_smtp_host='smarthost.rwth-aachen.de'):
        self.feedback_path = '.' + feedback_path if not platform.system() == 'Windows' and \
                                                    not feedback_path.startswith('.') else feedback_path

        self.mail_to = mail_to
        self.mail_from = mail_from
        self.mail_subject = mail_subject
        self.mail_smtp_host = mail_smtp_host

        super().__init__(feedback_name, questions, lang)

        self.submission_type = 'json'

    def save_entries(self):
        """
        Save entries into json file.

        Not used if user is in jupyter cluster.
        """

        if self.submission_type == 'json':
            if platform.system() == 'Windows':
                subprocess.check_call(['attrib', '-H', self.feedback_path])

            # write
            with open(self.feedback_path, mode='w', encoding='utf-8') as f:
                json.dump(self.entries, f)

            # hide again
            if platform.system() == 'Windows':
                subprocess.check_call(['attrib', '+H', self.feedback_path])

    def load_entries(self):
        if not os.path.isfile(self.feedback_path):
            # file does not exist, create
            with open(self.feedback_path, mode='w', encoding='utf-8') as f:
                json.dump([], f)

            # hide file
            if platform.system() == 'Windows':
                subprocess.check_call(['attrib', '+H', self.feedback_path])

        # load json file into self.entries
        with open(self.feedback_path, mode='r', encoding='utf-8') as f:
            self.entries = json.load(f)

    def send_mail(self):
        """
        Sends JSON file as attachment of a mail to predefined recipient

        Sets self.is_submitted to True if mail was sent successfully. False otherwise.
        """
        try:
            import smtplib
            from email.message import EmailMessage

            msg = EmailMessage()
            msg["From"] = self.mail_from
            msg["Subject"] = self.mail_subject if self.mail_subject is not None else self.feedback_name
            msg["To"] = self.mail_to

            with open(self.feedback_path, 'r') as f:
                msg.add_attachment(f.read(), filename=self.feedback_path)

            s = smtplib.SMTP(self.mail_smtp_host)
            s.send_message(msg)

            self.is_submitted = True

        except ConnectionRefusedError:
            # Not connected to the RWTH network
            self.output.clear_output()
            with self.output:
                print(self.feedback_text['mailfailure'])

            self.is_submitted = False

    def submit(self):
        # dump entries into json file
        # append only if not entry does not already exist in json file
        self.load_entries()
        if self.check_submission_status() == 'idle':
            self.entries.append(self.entry)
        self.save_entries()

        # try to send json file as attachment of mail
        if self.mail_to is not None:
            self.send_mail()

        # open and set statuses to submitted if mail is successfully sent
        if self.is_submitted:
            self.load_entries()

            for entry in self.entries:
                entry['status'] = 'submitted'

            self.save_entries()


class RWTHFeedbackCollector:
    """ RWTH Feedback Collector Class

    Processes json feedback files in a folder or feedbacks from RWTHJupyter realm and creates dataframes for every
        mentioned notebook.
    Intended to be used with RWTHFeedbackEvaluator but also standalone possible as the collected feedbacks are stored
        as pandas Dataframes.

    Examples
    --------
    >>> from rwth_nb.misc.feedback import RWTHFeedbackCollector
    >>> path_to_folder = './Feedbacks' # path to folder with feedback json files
    >>> collector = RWTHFeedbackCollector()
    >>> data = collector.get_all_folder(path_to_folder) # get feedback for all notebooks from folder
    >>> data = collector.get_all_jupyter(realm) # get feedback for all notebooks from RWTHJupyter realm
    """
    unparsed_entries = []

    def __init__(self):
        pass

    def __parse_entries(self, entries):
        for entry in entries:
            # skip faulty entries
            if not list(entry.keys()) == ['name', 'date', 'userhash', 'answer', 'types']:
                self.unparsed_entries.append(entry)
                continue

            # if a data frame already exists for given notebook work with this, create new if not
            if entry['name'] not in self.feedbacks.keys():
                self.feedbacks[entry['name']] = {'user': [], 'date': [], 'types': {}}

            notebook_dict = self.feedbacks[entry['name']]

            # check if user has submitted a feedback already for this notebook
            # if so check which date is more recent and add feedback to dataframe or remove existing
            if entry['userhash'] in notebook_dict['user']:
                index = notebook_dict['user'].index(entry['userhash'])
                existing_date = datetime.datetime.fromisoformat(notebook_dict['date'][index])
                new_date = datetime.datetime.fromisoformat(entry['date'])

                if existing_date > new_date:
                    # existing feedback is more recent, drop this one and continue with next entry in json file
                    continue
                else:
                    # this feedback is more recent -> remove existing feedback from dict
                    del notebook_dict['user'][index]
                    del notebook_dict['date'][index]
                    for key in entry['answer'].keys():
                        del notebook_dict[key][index]

            # create new entry for this submission in notebook dataframe
            notebook_dict['user'].append(entry['userhash'])
            notebook_dict['date'].append(entry['date'])

            for key, value in entry['answer'].items():
                try:
                    notebook_dict[key].append(value)
                except KeyError:
                    value_list = [value]
                    notebook_dict[key] = value_list

            notebook_dict['types'] = entry['types']

    def get_all_folder(self, folder_path: str) -> pd.DataFrame:
        """ Collect all DataFrames for every notebook from every json file in a path

        Parameters
        ----------
        folder_path: str
            Folder in which json feedback files are stored

        Returns
        -------
        pd.DataFrame
            pandas dataframe of all submitted feedback files in a folder
        """
        self.feedbacks = {}
        self.json_files = []
        assert os.path.isdir(folder_path), 'Folder path is not a directory!'

        # make a list of json files in directory
        for pos_json in os.listdir(folder_path):
            if pos_json.endswith('.json'):
                self.json_files.append(pos_json)

        assert len(self.json_files) > 0, 'No json file found.'

        for file in self.json_files:
            with open(os.path.join(folder_path, file), mode='r', encoding='utf-8') as f:
                entries = json.load(f)

                self.__parse_entries(entries)

        return pd.DataFrame(self.feedbacks)

    def get_all_jupyter(self, realm: str) -> pd.DataFrame:
        # Note that you need to be admin in order to successfully execute this code
        self.feedbacks = {}

        sub = Submission(realm)

        entries = [entry['data'] for entry in sub.get_all()]

        self.__parse_entries(entries)

        return pd.DataFrame(self.feedbacks)


class RWTHFeedbackEvaluator:
    """ RWTH Feedback Evaluator Class

    Processes pandas dataframes created with the collector class above into an evaluation interface.
    Likert scale like answers are plotted in different styles (bar only for now)
    Free text answers are collected and displayed into a list for readability

    Examples
    --------
    >>> from rwth_nb.misc.feedback import RWTHFeedbackEvaluator
    >>> eva = RWTHFeedbackEvaluator()
    >>> eva.evaluate(data, lang='de') # data: see rwth_nb.misc.feedback.RWTHFeedbackCollector
    """

    def __init__(self):
        pass

    def evaluate(self, data, lang='en'):
        """ Actual evaluation

        Parameters
        ----------
        data: pandas.Dataframe or List[pandas.Dataframe]
            dataframe created by collector class using json files
            multiple dataframes can be passed in a list (note that all must be in the same language)

        lang: str, optional
            language to be used; the likert scale is chosen accordingly from RWTHFeedback class
        """
        self.data = pd.concat(data, axis=1) if isinstance(data, list) else data

        if lang not in supported_languages:
            raise Exception('Language \'{}\' not supported. Supported languages are: {}'.format(lang, supported_languages))

        likert_scale = globals()['feedback_scale_options_' + lang]

        out = [widgets.Output() for _ in self.data]

        accordion = widgets.Accordion(children=out)
        for ind, d in enumerate(self.data):
            accordion.set_title(ind, d)
        display(accordion)

        for ind, d in enumerate(self.data):
            scale_options = self.data[d]['types']['scale']
            free_text_options = self.data[d]['types']['free-text']

            with out[ind]:
                # likert scale plots
                fig, axs = plt.subplots(1, len(scale_options), figsize=(13, 3))
                for i, l in enumerate(scale_options):
                    # list with counts
                    counts = [int(self.data[d][l].count(a)) for a in likert_scale]

                    # create dataframe x: likert-scale, y: counts
                    df = pd.Series(counts, index=likert_scale)

                    # plot for each option in scale_options
                    y_label = 'Anzahl' if lang == 'de' else 'Count'
                    axs[i].set_title(l)
                    axs[i].set_yticks(range(0, max(counts) + 2))
                    df.plot(kind='bar', ax=axs[i], ylabel=y_label, rot=15, fontsize=8, position=0.5,
                            color=rwth_colors['rwth:blue'])

                plt.tight_layout()

                # free text lists
                tab = widgets.Tab()
                tab_children = []
                for i, f in enumerate(free_text_options):
                    tab.set_title(i, f)

                    v_box = [widgets.HTML(f'<li>{label}</li>',
                                          description_width='initial') for
                             label in
                             self.data[d][f] if label.strip() not in ['', '-', '.', '/']]

                    tab_children.append(widgets.VBox(v_box))

                tab.children = tab_children
                display(tab)
