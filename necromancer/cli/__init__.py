"""
usage: git [--verbose] [--version] [--help]
           <command> [<args>...]

options:
   -h, --help

The most commonly used git commands are:
   r, raise      Raise a template

See 'git help <command>' for more information on a specific command.
"""
from docopt import docopt


if __name__ == '__main__':
    args = docopt(__doc__,
                  version='git version 1.7.4.4',
                  options_first=True)
    print('global arguments:')
    print(args)
    print('command arguments:')

    argv = [args['<command>']] + args['<args>']

    if args['<command>'] is in ['r', 'raise']:
        import raise_command
        print(docopt(raise_command.__doc__, argv=argv))
