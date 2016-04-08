'''
Rendering functions for templates.
'''
from random import choice
from pattern.en import tag, conjugate, PAST
import templates

mappings = {
    '#POS': "Positive Talking Points",
    '#NEG': "Negative Talking Points",
    '#NAME': "Character",
    '#GENDER': "Gender",
    }

def get_variables(tmpl):
    v = []
    for m in mappings:
        if m in tmpl:
            v.append((m, tmpl.count(m)))
    return v


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
    return choice(possible_templates)


def render_gender(character, tmpl):
    gender = character['Gender'][0]
    rendered = tmpl
    rendered = rendered.replace('#GPR', templates.GPR[gender])
    rendered = rendered.replace('#GNN', templates.GNN[gender])
    rendered = rendered.replace('#GPN', templates.GPN[gender])
    rendered = rendered.replace('#PNR', templates.PNR[gender])
    rendered = rendered.replace('#GPS', templates.GPS[gender])
    return rendered


def render_char_desc(character, tmpl):
    rendered = tmpl
    v = get_variables(tmpl)
    for e in v:
        used = []
        ch = character[mappings[e[0]]]
        for i in range(e[1]):
            var = choice(ch)
            while var in used:
                var = choice(ch)
            used.append(var)
            rendered = rendered.replace(e[0], var, 1)
    rendered = render_gender(character, rendered)
    return rendered

def render_location_desc(char1, char2, tmpl):
    pass

def simplepastify(in_string):
    '''
    params:
    :action_string: the underlying string representation (with underscores) to change to past tense

    returns the changed underlying string representation
    '''
    res = []

    def process(wrd):
        tmp = ''
        ignore_pos = ['IN', 'RP', 'TO']
        exception_lemma = ['flatter', 'flattered']
        if tag(wrd)[0][1] in ignore_pos:
            tmp = wrd
        elif any(wrd in ex_l for ex_l in exception_lemma):
            tmp = wrd
        else:
            tmp = conjugate(wrd, tense=PAST)
        return tmp

    for i in in_string.split('_'):
        res.append(process(i))
    return  '_'.join('%s' % r for r in res)


if __name__ == "__main__":
    import parse
    tmpls = templates.CHARACTER_DESCRIPTIONS
    noc = parse.parse_NOC()
    for c in noc:
        char = noc[c]
        tmpl = get_char_template(char, tmpls)
        if tmpl is None:
            print char
        print render_char_desc(char, tmpl)
