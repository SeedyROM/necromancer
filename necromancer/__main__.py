from docopt import docopt
from necromancer import cli
from necromancer.version import Version

version = Version("0.0.1")

if __name__ == '__main__':
    args = docopt(
        cli.__doc__,
        version=version.number,
        options_first=True
    )
    cli.parse_args(args)
