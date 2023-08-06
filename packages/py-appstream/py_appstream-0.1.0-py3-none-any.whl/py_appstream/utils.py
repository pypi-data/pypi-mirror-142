# SPDX-FileCopyrightText: 2022 Phu Hung Nguyen <phuhnguyen@outlook.com>
# SPDX-License-Identifier: LGPL-2.1-or-later

def localize(out_obj, node, f=None):
    lang = node.get('{http://www.w3.org/XML/1998/namespace}lang', node.get('lang', 'C'))
    if lang != 'x-test':
        out_obj[lang] = f(node.text) if f else node.text


def join_lines(txt: str):
    return ' '.join(txt.replace('\n', ' ').split())
