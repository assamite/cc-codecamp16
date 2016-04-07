'''
Rendering functions for templates.
'''
from random import choice

import templates

mappings = {
    '#POS': "Positive Talking Points",
    '#NEG': "Negative Talking Points",
    '#NAME': "Name",
    '#GENDER': "Gender",
    }

def get_variables(tmpl):
    v = []
    for m in mappings:
        if m in tmpl:
            v.append((m, tmpl.count(m)))
    print v


def get_char_template(character, templates):
    possible_templates = []
    for t in templates:
        v = get_variables(t)
        has_all = True
        for e in v:
            if len(character[mappings[e[0]]]) < e[1]:
                has_all = False
        if has_all:
            possible_templates.append(t)
    if len(possible_templates) == 0:
        return None
    tmpl = choice(possible_templates)


def render_char_desc(character, tmpl):
    rendered = tmpl
    v = get_variables(tmpl)
    for e in v:
        used = []
        ch = character[mappings[e[0]]]
        for i in e[1]:
            var = choice(ch)
            while var in used:
                var = choice(ch)
            used.append(var)
            rendered.replace(e[0], var, 1)
    return rendered



