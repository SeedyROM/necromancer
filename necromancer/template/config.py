import os
import toml
import sys

DEBUG = True


class ConfigException(BaseException):
    '''Base configuration exception
    '''


class TemplateDoesNotExist(ConfigException):
    '''Exception to be raised when the template does not exist
    '''


class InvalidConfiguration(ConfigException):
    '''Exception to be raise if the plug-in configuration is invalid
    '''


# TODO: Determine type from command line argument regex patterns
def find_plugin(path, plugin_type='local'):
    '''Determine if the specified plug-in exists

    Args:
        @path(str) : 'The path of the plug-in
        @type(str) default 'local' : 'The location of the plug-in
    '''

    if plugin_type == 'local':
        find_local_plugin(path)
    else:
        raise InvalidConfiguration('Invalid plug-in type')


def load_plugin_config(path):
    '''Determine if the path is a proper necromancer plug-in

    Args:
        @path(str) : 'The path of the plug-in
    '''


def find_local_plugin(path):
    ''' Find a plug in the local file system

    Args:
        @path(str) : The path of the plug-in
    '''
    absolute_path = os.path.abspath(
        os.path.join(os.getcwd(), path)
    )

    if not os.path.exists(absolute_path):
        raise TemplateDoesNotExist(f'Template does not exist {absolute_path}')

    if DEBUG:
        print(absolute_path)

    return absolute_path
