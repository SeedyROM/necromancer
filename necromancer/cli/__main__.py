"""
usage: necro [--version] [--verbose]
             [<command>] [<args>...]

options:
   -V,  --version
   -v,  --verbose

The most commonly used git commands are:
   h, help       Display help
   r, raise      Raise a template

See 'git help <command>' for more information on a specific command.
"""
import chalk
import runpy
from subprocess import call
from docopt import docopt

args = docopt(__doc__,
              version='neco 0.0.1',
              options_first=True)

argv = [args['<command>']] + args['<args>']

if args['<command>'] in ['r', 'raise']:
    exit(
        call(['python', '-m', 'necromancer.cli.raise_command'] + argv)
    )
elif args['<command>'] in ['h', 'help', None]:
    exit(
        __doc__
    )
else:
    exit(
        chalk.yellow(
            f"'{args['<command>']}' is not a necro command. See 'necro help'."
        )
    )
