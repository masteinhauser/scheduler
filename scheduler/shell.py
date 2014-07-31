#!/usr/bin/env python2
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import argh
import configparser

from scheduler import log


LOG = log.get_logger()


def main():
    """ Entry point for all things necc-scheduler """

    commands = []

    parser = argh.ArghParser()
    parser.add_commands(commands)
    parser.add_argument('-d', '--debug', action='store_true',
                        help='Set logging level to DEBUG')
    parser.add_argument('-V', '--version', action='store_true',
                        help='Display version in output')
    parser.dispatch()


if __name__ == '__main__':
    main()
