from base import TwoParamWorkflow
import common


class SampleWorkflow(TwoParamWorkflow):

    def __init__(self, wf, params):
        super(SampleWorkflow, self).__init__(wf, params)

    def execute_with_two_param(self, v1, v2):
        self.add_item('{} {}'.format(v1, v2))

    def get_icon_path(self):
        return common.ICON_DEFAULT
