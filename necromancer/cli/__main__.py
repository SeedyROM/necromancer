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
from docopt import docopt

args = docopt(__doc__,
              version='neco 0.0.1',
              options_first=True)

argv = [args['<command>']] + args['<args>']

if args['<command>'] in ['r', 'raise']:
    from necromancer.cli import raise_command
    print(docopt(raise_command.__doc__, argv=argv))
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
