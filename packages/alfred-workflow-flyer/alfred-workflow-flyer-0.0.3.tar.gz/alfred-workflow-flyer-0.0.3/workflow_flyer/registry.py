conf = {}


def register_config(new_conf):
    global conf
    conf = new_conf


def search_handler(cmd):
    commands = []
    if cmd == 'all' or cmd == 'ALL':
        return conf.keys(), True

    if cmd in conf:
        commands.append(cmd)
        return commands, False

    for each in conf.keys():
        if each.startswith(cmd):
            commands.append(each)
    return commands, True


def get_handler(name):
    if name not in conf:
        raise Exception('cannot found handler: {}'.format(name))
    return conf[name]


def get_handle_size():
    return len(conf)
