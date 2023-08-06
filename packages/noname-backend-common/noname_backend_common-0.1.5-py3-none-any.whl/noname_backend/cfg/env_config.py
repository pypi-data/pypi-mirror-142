import os

class EnvironmentConfig:
    def __init__(self, prefix, delimiter='_'):
        self._prefix = prefix
        self._delimiter = delimiter

    def __getitem__(self, key):
        return EnvironmentSection(self._prefix, key, self._delimiter)

class EnvironmentSection:
    def __init__(self, prefix, section, delimiter):
        self._prefix = prefix
        self._section = section
        self._delimiter = delimiter

    def __getitem__(self, key):
        try:
            converted_key = self._convert_key(key)
            return os.environ[converted_key]
        except KeyError:
            return None

    def _convert_key(self, key):
        return self._delimiter.join([
            self._prefix,
            self._section.upper(),
            key.upper()
        ])
