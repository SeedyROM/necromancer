'''
Usage: necro shell|s USER_COMMAND

Options
    USER_COMMAND        a command in the .necro.toml
'''

from docopt import docopt


if __name__ == '__main__':
    print(docopt(__doc__))
