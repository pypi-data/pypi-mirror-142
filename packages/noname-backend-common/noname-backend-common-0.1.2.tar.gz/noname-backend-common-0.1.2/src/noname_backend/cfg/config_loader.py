import configparser

class ConfigLoader:
    def __init__(self, config_path):
        self._config_path = config_path

    def load(self):
        config = configparser.ConfigParser()
        config.read(self._config_path)
        return config
