import glob
import json
import os
import sys

from necromancer.template.config import (
    find_plugin,
    load_plugin_config
)


class CLI:

    @staticmethod
    def parse_args():
        path = './dsjadjsakjd'

        try:
            find_plugin(path)
            load_plugin_config(path)
        except:
            
