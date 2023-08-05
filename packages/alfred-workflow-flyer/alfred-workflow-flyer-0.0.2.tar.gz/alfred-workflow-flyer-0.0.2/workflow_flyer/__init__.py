import sys
from workflow import Workflow3
from workflow_flyer.dispatcher import main


def run():
    workflow = Workflow3()
    sys.exit(workflow.run(main))
