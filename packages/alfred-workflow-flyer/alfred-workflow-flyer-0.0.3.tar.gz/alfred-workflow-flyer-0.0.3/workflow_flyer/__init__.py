import sys
from workflow import Workflow3
from workflow_flyer.dispatcher import main
from workflow_flyer import registry


def run():
    if not registry.conf or len(registry.conf) == 0:
        raise Exception('The registry cannot be empty')

    workflow = Workflow3()
    sys.exit(workflow.run(main))
