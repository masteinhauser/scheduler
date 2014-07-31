# vim: tabstop=4 shiftwidth=4 softtabstop=4
from scheduler import config
from scheduler import log

LOG = log.get_logger()

TEACHERS = []
STUDENTS = []
TASKS = dict()


def add_teachers():
    return


def add_students():
    return


def add_tasks():
    return


def add_groups():
    return

def schedule():
    scheduled = OrderedDict()

    config.command_init(**kwargs)

    add_teachers()
    add_students()
    add_tasks()


    return schedule
