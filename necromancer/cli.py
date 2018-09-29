"""Necromancer: A project boilerplate tool-kit!"

Usage:
  necro ship [r[aise]] <plugin-or-path>...
  necro (-h | --help)
  necro --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
import chalk
from necromancer.template import config


class CLI:

    @staticmethod
    def parse_args(**kwargs):
        path = kwargs['path']
        try:
            config.find_plugin(path)
            config.load_plugin_config(path)
        except config.ConfigException as e:
            print(chalk.red('Nonexistant or invalid template specified!'))
