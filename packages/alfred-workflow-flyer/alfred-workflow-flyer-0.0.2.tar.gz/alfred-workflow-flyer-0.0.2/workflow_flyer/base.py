import common
from workflow.notify import notify as wf_notify


class BaseWorkflow(object):

    def __init__(self, wf, params):
        self.wf = wf
        self.params = params

    def execute(self):
        self.show_tips('Hello World')

    def add_item(self, title, sub_title=None, copy_text=None, autocomplete=None):
        self.wf.add_item(
            title=title,
            subtitle=sub_title or '',
            arg=copy_text or '',
            autocomplete=autocomplete,
            valid=True,
            icon=self.get_icon_path()
        )

    def show_tips(self, msg):
        common.show_tips(self.wf, msg)

    def show_warning(self, msg):
        common.show_warning(self.wf, msg)

    def show_error(self, msg, content=''):
        common.show_error(self.wf, msg, content)

    @staticmethod
    def notify(title, content, sound=None):
        wf_notify(title, content, sound=sound)

    def logger(self):
        return self.wf.logger

    def get_icon_path(self):
        return common.ICON_DEFAULT

    def get_desc(self):
        return 'No any description'


class SingleParamWorkflow(BaseWorkflow):

    def __init__(self, wf, params):
        super(SingleParamWorkflow, self).__init__(wf, params)

    def execute(self):
        if len(self.params) < 1:
            self.show_tips('The value is required')
            return

        first_param = self.params[0]
        if not first_param:
            self.show_tips('The first param is empty')
            return
        self.execute_with_single_param(first_param)

    def execute_with_single_param(self, value):
        raise Exception('unsupported method')


class TwoParamWorkflow(BaseWorkflow):

    def __init__(self, wf, params):
        super(TwoParamWorkflow, self).__init__(wf, params)

    def execute(self):
        if len(self.params) < 1:
            self.show_tips('The value is required')
            return

        if len(self.params) < 2:
            self.show_tips('The second param is required')
            return

        first_param = self.params[0]
        second_param = self.params[1]
        if not first_param or not second_param:
            self.show_tips('The param is empty')
            return
        self.execute_with_two_param(first_param, second_param)

    def execute_with_two_param(self, v1, v2):
        raise Exception('unsupported method')


class ThirdParamWorkflow(BaseWorkflow):
    def __init__(self, wf, params):
        super(ThirdParamWorkflow, self).__init__(wf, params)

    def execute(self):
        if len(self.params) < 1:
            self.show_tips('The value is required')
            return

        if len(self.params) < 2:
            self.show_tips('The second param is required')
            return

        if len(self.params) < 3:
            self.show_tips('The third param is required')
            return

        first_param = self.params[0]
        second_param = self.params[1]
        third_param = self.params[2]
        if not first_param or not second_param or not third_param:
            self.show_tips('The param is empty')
            return
        self.execute_with_third_param(first_param, second_param, third_param)

    def execute_with_third_param(self, v1, v2, v3):
        raise Exception('unsupported method')
