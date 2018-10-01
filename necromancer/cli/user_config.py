'''
open and return a user config
'''


import os
import toml


def open_toml_file(user_settings):
    ''' open a file and return a toml object '''

    return toml.load(user_settings)


def find_user_settings():
    '''
    first XDG_CONFIG_HOME/necromancer
    if the var is not set look in ~/.config/necromancer
    then ~/.necromancer
    '''

    home = os.path.expanduser('~')

    config_home = None

    # TODO: this is bad and i fell bad
    if os.environ.get('XDG_CONFIG_HOME'):
        config_home = os.path.join(
            os.environ.get('XDG_CONFIG_HOME'), 'necromancer')

    elif os.path.exists(os.path.join(home, '.config', 'necromancer')):
        config_home = os.path.join(home, '.config', 'necromancer')

    elif os.path.exists(os.path.join(home, '.necromancer')):
        config_home = os.path.join(home, '.necromancer')

    else:
        return None

    return config_home


def get_config():
    ''' get the user config or none '''

    user_settings = find_user_settings

    user_conf = open_toml_file(user_settings)

    print(user_conf)
