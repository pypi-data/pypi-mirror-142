import workflow
import os

ICON_BASE_DIR = os.path.abspath(os.path.dirname(__file__)) + '/static'

ICON_DEFAULT = workflow.ICON_INFO
ICON_TIPS = os.path.join(ICON_BASE_DIR, 'tips.png')
ICON_WARNING = os.path.join(ICON_BASE_DIR, 'warning.png')
ICON_ERROR = workflow.ICON_ERROR


def show_tips(wf, msg):
    wf.add_item(msg, '', arg='', valid=True, icon=ICON_TIPS)


def show_warning(wf, msg):
    wf.add_item(msg, '', arg='', valid=True, icon=ICON_WARNING)


def show_error(wf, msg, content=''):
    wf.add_item(msg, content, arg='', valid=True, icon=ICON_ERROR)
