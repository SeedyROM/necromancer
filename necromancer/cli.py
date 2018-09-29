"""Necromancer: A project boilerplate tool-kit!"

Usage: necro <command> [<args>...]

Commands:
    r raise <path> Raise a template from a plug-in

Options:
    -h --help        Show this screen
    -v --version     Show version
"""
import chalk
from necromancer.template import config


def parse_args(args):
    try:
        print(args)
    except config.ConfigException as e:
        print(chalk.red('Template Error:'))
        print(chalk.red('---------------'))
        print(chalk.yellow(e))

