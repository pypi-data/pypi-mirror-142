# SPDX-FileCopyrightText: 2022 Phu Hung Nguyen <phuhnguyen@outlook.com>
# SPDX-License-Identifier: LGPL-2.1-or-later

from __future__ import annotations

import dateutil.parser

from . import utils
from .exceptions import AppStreamParseError


class Node(object):
    NOT_TO_SERIALIZE = []

    def parse_tree(self, node):
        pass

    def serialize(self):
        obj = {}
        for a, v in vars(self).items():
            if a not in type(self).NOT_TO_SERIALIZE and v:
                obj[a] = v
        return obj


class Description(Node):
    def __init__(self):
        self.object = {}

    def _prep_lang(self, n):
        lang = n.get('{http://www.w3.org/XML/1998/namespace}lang', n.get('lang', 'C'))
        if lang != 'x-test' and lang not in self.object:
            self.object[lang] = ''
        return lang

    def parse_tree(self, node):
        for n in node:
            if n.tag == 'p':
                lang = self._prep_lang(n)
                if lang == 'x-test':
                    continue
                self.object[lang] += f'<p>{utils.join_lines(n.text)}</p>\n'
            elif n.tag in ['ol', 'ul']:
                langs = set()
                for c in n:
                    if c.tag == 'li':
                        lang = self._prep_lang(c)
                        if lang == 'x-test':
                            continue
                        langs.add(lang)
                        if not (self.object[lang].endswith('</li>\n') or self.object[lang].endswith(f'<{n.tag}>\n')):
                            self.object[lang] += f'<{n.tag}>\n'
                        self.object[lang] += f'<li>{utils.join_lines(c.text)}</li>\n'
                    else:
                        raise AppStreamParseError(f'Expected <li> in <{n.tag}>, got <{c.tag}>')
                for lang in langs:
                    self.object[lang] += f'</{n.tag}>\n'
            else:
                raise AppStreamParseError(f'Expected <p>, <ul>, <ol> in <{node.tag}>, got <{n.tag}>')
        # only accept languages with number of parts not less than number of 'C' parts
        lang_part_counts = list(map(lambda item: (item[0], len(item[1].split('\n'))), self.object.items()))
        # max_part_count = max(lang_part_counts, key=lambda x: x[1])[1]
        c_part_count = len(self.object['C'].split('\n'))
        unfit_langs = list(map(lambda p: p[0], filter(lambda p: p[1] < c_part_count, lang_part_counts)))
        for lang in unfit_langs:
            self.object.pop(lang)
        for lang in self.object:
            self.object[lang] = self.object[lang].strip()

    def serialize(self):
        return self.object


class Artifact(Node):
    def __init__(self):
        self.type = ''
        self.platform = ''
        self.bundle = ''
        self.locations = []
        self.checksum = {}
        self.size = {}
        # self.filename = ''

    def parse_tree(self, node):
        """ Parse a <artifact> object """
        self.type = node.get('type')
        self.platform = node.get('platform', '')
        self.bundle = node.get('bundle', '')
        for c4 in node:
            if c4.tag == 'location':
                self.locations.append(c4.text)
            elif c4.tag == 'checksum':
                self.checksum[c4.get('type')] = c4.text
            elif c4.tag == 'size':
                if c4.get('type') == 'download':
                    self.size['download'] = int(c4.text)
                elif c4.get('type') == 'installed':
                    self.size['installed'] = int(c4.text)


class Release(Node):
    not_to_serialize = ['timestamp', 'date']

    def __init__(self):
        self.version = ''
        self.timestamp = 0
        self.date = ''
        self.unix_timestamp = 0
        # self.date_eol = ''
        # self.urgency = 'medium'
        self.type = 'stable'
        self.description = None
        self.url: dict[str, str] = {}
        # self.issues = []
        self.artifacts: list[Artifact] = []

    def parse_tree(self, node):
        """ Parse a <release> object """
        if 'timestamp' in node.attrib:
            self.timestamp = int(node.attrib['timestamp'])
        if 'date' in node.attrib:
            self.date = node.get('date')
        if self.timestamp:
            self.unix_timestamp = self.timestamp
        elif self.date:  # 'timestamp' takes precedence over 'date'
            dt = dateutil.parser.parse(self.date)
            self.unix_timestamp = int(dt.strftime("%s"))
        if 'version' in node.attrib:
            self.version = node.attrib['version']
            # fix up hex value
            if self.version.startswith('0x'):
                self.version = str(int(self.version[2:], 16))
        self.type = node.get('type', 'stable')
        for c3 in node:
            if c3.tag == 'description':
                self.description = Description()
                self.description.parse_tree(c3)
            elif c3.tag == 'url':
                t = c3.get('type', 'details')
                self.url = {t: c3.text}
            elif c3.tag == 'artifacts':
                for c4 in c3:
                    a = Artifact()
                    a.parse_tree(c4)
                    self.artifacts.append(a)

    def serialize(self):
        obj = {}
        for a, v in vars(self).items():
            if a not in type(self).not_to_serialize and v:
                serial_a = 'unix-timestamp' if a == 'unix_timestamp' else a
                obj[serial_a] = self.description.serialize() if a == 'description' \
                    else [x.serialize() for x in self.artifacts] if a == 'artifacts' \
                    else v
        return obj


class Image(Node):
    not_to_serialize = ['type']

    def __init__(self):
        self.type = ''
        self.width = 0
        self.height = 0
        # xml:lang
        self.url = ''

    def parse_tree(self, node):
        """ Parse a <image> object """
        self.type = node.get('type', '')
        self.width = int(node.get('width', 0))
        self.height = int(node.get('height', 0))
        self.url = node.text


class Screenshot(Node):
    def __init__(self):
        self.default = False
        self.caption = {}
        self.thumbnails = []
        self.source = None

    def parse_tree(self, node):
        """ Parse a <screenshot> object """
        self.default = node.get('type', '') == 'default'
        for c3 in node:
            if c3.tag == 'caption':
                utils.localize(self.caption, c3)
            elif c3.tag == 'image':
                im = Image()
                im.parse_tree(c3)
                if im.type == 'thumbnail':
                    self.thumbnails.append(im)
                else:
                    self.source = im

    def serialize(self):
        obj = {}
        for a, v in vars(self).items():
            if a not in type(self).NOT_TO_SERIALIZE and v:
                serial_a = 'source-image' if a == 'source' else a
                obj[serial_a] = self.source.serialize() if a == 'source' \
                    else [x.serialize() for x in self.thumbnails] if a == 'thumbnails' \
                    else v
        # video
        return obj


class Provide(Node):
    TYPES = {
        'mediatype': 'mediatypes',
        'library': 'libraries',
        'font': 'fonts',
        'modalias': 'modalaliases',
        'firmware': 'firmwares',
        'python2': 'python2',
        'python3': 'python3',
        'dbus': 'dbus',
        'binary': 'binaries',
        'id': 'ids'
    }

    def __init__(self):
        for v in self.TYPES.values():
            setattr(self, v, [])

    def parse_tree(self, node):
        """ Parse a <provide> object """
        for c2 in node:
            if c2.tag in self.TYPES:
                attr = self.TYPES[c2.tag]
                current = getattr(self, attr)
                current.append(c2.text)
                setattr(self, attr, current)


class ContentRating(Node):
    def __init__(self):
        self.type = ''
        self.attributes = {}

    def parse_tree(self, node):
        self.type = node.get('type', 'oars-1.0')
        for c2 in node:
            if c2.tag == 'content_attribute' and 'id' in c2.attrib:
                self.attributes[c2.get('id')] = c2.text

    def serialize(self):
        return {self.type: self.attributes}
