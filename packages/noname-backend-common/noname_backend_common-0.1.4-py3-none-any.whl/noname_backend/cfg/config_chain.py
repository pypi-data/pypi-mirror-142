class ConfigChain:
    def __init__(self, chain):
        self._chain = chain

    def __getitem__(self, key):
        return ConfigChainSection(self._chain, key)

class ConfigChainSection:
    def __init__(self, chain, section):
        self._chain = chain
        self._section = section

    def __getitem__(self, key):
        for cfg in self._chain:
            section = _get_or_none(cfg, self._section)
            if section is not None:
                value = _get_or_none(section, key)
                if value is not None:
                    return value
        raise KeyError(f'{key} not found')

def _get_or_none(config, key):
    try:
        return config[key]
    except KeyError:
        return None
