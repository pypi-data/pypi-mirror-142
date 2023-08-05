import common
import sys
import registry

reload(sys)
sys.setdefaultencoding('utf8')


def __execute(wf, cmd, params):
    logger = wf.logger

    commands, fuzzy = registry.search_handler(cmd)
    logger.info('commands: {}'.format(commands))
    if len(commands) == 0:
        return common.show_warning(wf, 'Cannot found command: {}'.format(cmd))

    if fuzzy and registry.get_handle_size() > 1:
        for c in commands:
            handle = registry.get_handler(c)
            instance = handle(wf, params)
            wf.add_item(c, instance.get_desc(), autocomplete=c, icon=instance.get_icon_path())
        return

    handler = registry.get_handler(commands[0])
    instance = handler(wf, params)
    instance.execute()


def main(wf):
    logger = wf.logger
    args = sys.argv
    logger.info('input args: {}'.format(sys.argv))

    if len(args) < 2:
        common.show_tips(wf, 'The command is required')
        wf.send_feedback()
        return

    cmd = args[1]
    params = []
    if len(args) >= 2:
        params = args[2:]

    logger.info('cmd: {}, params: {}'.format(cmd, params))
    try:
        __execute(wf, cmd, params)
    except Exception as e:
        logger.exception(e)
        common.show_error(wf, 'Fail to execute handler', str(e))
    finally:
        wf.send_feedback()
