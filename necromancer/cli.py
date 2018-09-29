"""Necromancer: A project boilerplate tool-kit!"

Usage: necro <command> [<args>...]

Commands:
    r raise          Raise a template from a plug-in

Options:
    -h --help        Show this screen
    -v --version     Show version
"""
import chalk
from necromancer.template import config


def parse_args(**kwargs):
    path = kwargs['<path>']
    try:
        config.find_plugin(path)
        config.load_plugin_config(path)
    except config.ConfigException as e:
        print(chalk.red('Template Error:'))
        print(chalk.red('---------------'))
        print(chalk.yellow(e))
