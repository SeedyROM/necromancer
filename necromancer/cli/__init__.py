"""
Usage:
    necro [--version] [--verbose] [--help]
          <command> [<args>...]

Options:
   -V,  --version
   -v,  --verbose
   -h,  --help

Necromancer commands:
   r, raise      Raise a template
   s, shell      Run a shell command as described in PROJECT/.necro.toml

See 'necro <command> --help' for more information on a specific command.
"""

import chalk
from docopt import docopt

from . import (raise_command, shell_command, fake_builder)

# pylint: disable=invalid-name
raise_module = fake_builder.fake_builder_raise
shell_module = fake_builder.fake_builder_shell

# pylint: disable=invalid-name
red = chalk.Chalk('red')
red_bold = red + chalk.utils.FontFormat('bold')
yellow = chalk.Chalk('yellow')


def runner():
    ''' parse args then call the right function '''
    args = docopt(__doc__, version='necro 0.0.1', options_first=True)

    argv = [args['<command>'], *args['<args>']]

    # the args to add to the build_obj
    return_code = 1

    if args['<command>'] in ['r', 'raise']:
        run_args = docopt(raise_command.__doc__, argv=argv)
        return_code = raise_module(run_args)

    elif args['<command>'] in ['s', 'shell']:
        run_args = docopt(shell_command.__doc__, argv=argv)
        return_code = shell_module(run_args)

    else:
        head_msg = red_bold('Error')
        cmd_with_color = yellow(args["<command>"])
        warn_msg = f'\n{head_msg}: there is no command {cmd_with_color}\n'
        print(__doc__, warn_msg)
        return 1

    return return_code
