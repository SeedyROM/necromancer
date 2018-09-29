import glob
import json
import os
import sys
import chalk

from necromancer.template.config import (
    ConfigException,
    find_plugin,
    load_plugin_config
)


class CLI:

    @staticmethod
    def parse_args(**kwargs):

        try:
            find_plugin(path)
            load_plugin_config(path)
        except ConfigException as e:
            print(chalk.red('Nonexistant or invalid template specified!'))
