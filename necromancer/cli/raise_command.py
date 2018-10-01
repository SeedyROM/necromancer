"""
Usage:
    necro raise|r <filepattern> <location>

Options:
    -h,  --help         this help message
    -l,  --local        TODO

    <filepattern>       the file patter to build, see Defaults
    <location>          the path to the pronject ending in its name
                            e.g.  project_dir/example_name

Defaults:
    py[thon]
    ja[vascript]

Examples:
    necro raise python work/example_lib

    necro r ja /home/user/work/a_different_example_lib
"""
import chalk
from docopt import docopt
from necromancer.template import plug_in


if __name__ == '__main__':
    args = docopt(__doc__)
