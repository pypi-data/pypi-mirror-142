from typing import Dict

class EngineConfigMeta(type):
    """
        class LocalEngineConfig(metaclass=EngineConfigMeta):
            engine_id: str = 'mcd-example-engine-py'
            engine_name: str = 'A human friendly summary.'

            code_version: int = 7
            extra_deps: Dict[str, str] = {
                'extra-library': '2.8.1',
            }
    """
    engine_id: str = ''
    engine_name: str = ''
    code_version: int = -1
    extra_deps: Dict[str, str] = {}

    def __new__(cls, name, bases, defs, **kwargs):
        for key in filter(lambda x: x[0] != '_', cls.__dict__):
            if key not in defs:
                text = f'Engine Config Error: {key} not found'
                print(text); raise NotImplementedError(text)
            elif not isinstance(defs[key], type(getattr(cls, key))):
                text = f'Engine Config Error: {key} type mismatch'
                print(text); raise TypeError(text)
        return super(EngineConfigMeta, cls).__new__(cls, name, bases, defs, **kwargs)


class _ExampleEngineConfig(metaclass=EngineConfigMeta):
    engine_id: str = 'mcd-example-engine-py'
    engine_name: str = 'A human friendly summary.'
    code_version: int = 7
    extra_deps: Dict[str, str] = {
        'extra-library': '2.8.1',
    }
