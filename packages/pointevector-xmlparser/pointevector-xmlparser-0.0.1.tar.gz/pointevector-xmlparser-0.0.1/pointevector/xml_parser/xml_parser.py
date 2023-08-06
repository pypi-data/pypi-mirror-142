import io
import logging
import xml.sax
from xml.sax.handler import ContentHandler

from pointevector.xml_parser.validate_config import ParserConfig

class StopSaxProcessing(xml.sax.SAXException):
    pass

class DynamicHandler(ContentHandler):
    def __init__(self, config: ParserConfig):
        self.config = config
        self.attributes_remaining = set(config.get('attributes', {}))
        self.content_remaining = set(config.get('content', {}))
        self.object_context = {}
        self.data = {}

    def startDocument(self):
        self.path = ()
        return super().startDocument()

    def _check_remaining(self):
        to_check = (
            'attributes_remaining',
            'content_remaining',
        )
        return {c: getattr(self, c) for c in to_check if len(getattr(self, c)) > 0}

    def _gen_attributes(self, attrs):
        for a, data in self.config.get('attributes', {}).items():
            for path in data.get('paths', []):
                if self.path == tuple(path) and data['name'] in attrs.getNames():
                    yield a, attrs.getValue(data['name'])

    def _find_object(self):
        for o, data in self.config.get('object_lists', {}).items():
            for path in data.get('paths', []):
                if self.path == tuple(path):
                    return {'name': o, 'path': tuple(path), 'partial': {}}
        return {}

    def startElement(self, name, attrs):
        self.path += (name,)
        # Attributes
        if len(self.attributes_remaining) > 0:
            for a, v in self._gen_attributes(attrs):
                self.data[a] = v
                self.attributes_remaining -= {a,}
        # Object lists
        obj = self._find_object()
        if obj:
            self.object_context = obj
            logging.info(f"Set object context: {self.object_context}")
        return super().startElement(name, attrs)

    def characters(self, content):
        # Content
        if len(self.content_remaining) > 0:
            for c, paths in self.config.get('content', {}).items():
                for path in paths:
                    if self.path == tuple(path):
                        self.data[c] = content.strip()
                        self.content_remaining -= {c,}
        # Object lists
        if self.object_context:
            for name, paths in self.config['object_lists'][self.object_context['name']]['fields'].items():
                for path in paths:
                    if self.path == self.object_context['path'] + tuple(path):
                        self.object_context['partial'][name] = content.strip()
        return super().characters(content)

    def endElement(self, name):
        self.path = self.path[:-1]
        # Object lists
        if self.object_context and self.path == self.object_context['path'][:-1]:
            obj_name = self.object_context['name']
            if obj_name not in self.data:
                self.data[obj_name] = []
            self.data[obj_name].append(self.object_context['partial'])
            self.object_context = {}
        return super().endElement(name)

    def endDocument(self):
        return super().endDocument()

def parse(config: ParserConfig, data: io.BytesIO):
    h = DynamicHandler(config)
    parser = xml.sax.make_parser()
    parser.setContentHandler(h)
    try:
        parser.parse(data)
    except StopSaxProcessing:
        pass
    return h.data
