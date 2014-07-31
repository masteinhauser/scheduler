# vim: tabstop=4 shiftwidth=4 softtabstop=4


LOG = log.get_logger()


def command_init(**kwargs):
    """"""
    if 'debug' in kwargs and kwargs['debug']:
        log.set_level_debug()
