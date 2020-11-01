import configparser
import os


class EnvInterpolation(configparser.BasicInterpolation):
    """Interpolation which expands environment variables in values."""

    def before_get(self, parser, section, option, value, defaults):
        return os.path.expandvars(value)


def load_config():
    """
    loading config values from local.ini
    :return:
    """
    project_dir = os.path.abspath(
        os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), '..'), 'config'), 'local.ini'))
    config = configparser.ConfigParser()
    config.read(project_dir)
    server = config['MAIN']

    return server
