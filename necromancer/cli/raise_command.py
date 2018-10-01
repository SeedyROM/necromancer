"""usage: necro raise <location> <filepattern>

Options:
    -h,  --help
    -l,  --local
"""
import chalk
from docopt import docopt
from necromancer.template import config

if __name__ == '__main__':
    args = docopt(__doc__)
    plugin_type = args['<location>']
    filepattern = args['<filepattern>']

    try:
        config.find_plugin(filepattern, plugin_type=plugin_type)
    except BaseException as e:
        print(chalk.red('Failed to raise plugin:'))
        print(chalk.red('----------------------'))
        print(e)
