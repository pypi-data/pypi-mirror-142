from typing_extensions import NotRequired, TypedDict
from typing import Dict, List

def _check_for_unknown_keys(cls, config: dict):
    for key in config:
        if key not in cls.__annotations__:
            raise TypeError(f"Unknown key in {cls} configuration: {key}")

MultiPath = List[List[str]]

class ParserAttribute(TypedDict):
    name: str
    paths: MultiPath

MultiPathMap = Dict[str, MultiPath]
AttributeMap = Dict[str, ParserAttribute]
def _multipath(paths):
    for path in paths:
        for item in path:
            if not isinstance(item, str):
                raise TypeError('Path must be a list of only strings')

def _attribute_map(d: dict):
    for attribute, data in d.items():
        if not isinstance(attribute, str):
            raise TypeError('Attribute name must be a string')
        if 'name' not in data:
            raise KeyError('Attribute object must have a "name"')
        _multipath(data['paths'])

def _multipath_map(d: dict) -> MultiPathMap:
    for content, paths in d.items():
        if not isinstance(content, str):
            raise TypeError('Map item name must be a string')
        _multipath(paths)

class Object(TypedDict):
    fields: MultiPathMap
    paths: MultiPath

class ParserConfig(TypedDict):
    attributes: NotRequired[Dict[str, ParserAttribute]]
    content: NotRequired[Dict[str, MultiPath]]
    object_lists: NotRequired[Dict[str, Object]]

def _object_list(d: dict):
    for name, data in d.items():
        if not isinstance(name, str):
            raise TypeError('Object name must be a string')
        _multipath_map(data['fields'])
            

def validate(config: Dict) -> ParserConfig:
    if config:
        _check_for_unknown_keys(ParserConfig, config)
        if 'attributes' in config:
            _attribute_map(config['attributes'])
        if 'content' in config:
            _multipath_map(config['content'])
        if 'object_lists' in config:
            _object_list(config['object_lists'])
    return config
