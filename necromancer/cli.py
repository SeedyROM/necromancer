"""Necromancer: A project boilerplate tool-kit!"

Usage:
  necro raise <path>
  necro (-h | --help)
  necro --version

Options:
  -h --help     Show this screen.
  --version     Show version.
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
        print(chalk.yellow('Nonexistant or invalid template specified!'))
