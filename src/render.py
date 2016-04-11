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

loc_mappings = {
    '#POS_LOC': 'Location',
    '#NEUT_LOC': 'Location',
    '#NEG_LOC': 'Location',
    '#POS_AMB': 'Ambience',
    '#NEUT_AMB': 'Ambience',
    '#NEG_AMB': 'Ambience'
}

def get_loc_variables(tmpl):
    v = []
    for m in loc_mappings:
        if m in tmpl:
            v.append((m, tmpl.count(m)))
    return v

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


def render_gender(character, tmpl, character2=None):
    gender = character['Gender'][0]
    rendered = tmpl
    rendered = rendered.replace('#GPR', templates.GPR[gender])
    rendered = rendered.replace('#GNN', templates.GNN[gender])
    rendered = rendered.replace('#GPN', templates.GPN[gender])
    rendered = rendered.replace('#PNR', templates.PNR[gender])
    rendered = rendered.replace('#GPS', templates.GPS[gender])
    if character2 is not None:
        gender = character2['Gender'][0]
        rendered = rendered.replace('#NOP', templates.NOP[gender])
        #rendered = rendered.replace('#GNN', templates.GNN[gender])
        #rendered = rendered.replace('#GPN', templates.GPN[gender])
        #rendered = rendered.replace('#PNR', templates.PNR[gender])
        #rendered = rendered.replace('#GPS', templates.GPS[gender])
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

def get_char_desc(character, templates, *args, **kwargs):
    tmpl = get_char_template(character, templates)
    return render_char_desc(character, tmpl)


def get_location_template(loc, templates):
    possible_templates = []
    mood = loc['Mood']
    for e in templates:
        if '#NEUT_LOC' in e and mood == 'NEUT':
            possible_templates.append(e)
        if '#POS_LOC' in e and mood == 'POS':
            possible_templates.append(e)
        if '#NEG_LOC' in e and mood == 'NEG':
            possible_templates.append(e)
    return choice(possible_templates)


def render_location_desc(char1, char2, location, tmpl):
    
    mood = location['Mood']
    loc = location['Location']
    det = location['Determiner']
    prep = location['Preposition']
    amb = location['Ambience']
    n1 = char1['Character'][0]
    n2 = char2['Character'][0]

    rendered = tmpl
    rendered = rendered.replace('#DET', det)
    rendered = rendered.replace('#PREP', prep)
    rendered = rendered.replace('#NAME', n1)
    rendered = rendered.replace('#NOM', n2)

    if mood == 'NEUT':
        rendered = rendered.replace('#NEUT_LOC', loc)
        used = []
        while '#NEUT_AMB' in rendered:
            var = choice(amb)
            while var in used:
                var = choice(amb)
            used.append(var)
            rendered = rendered.replace('#NEUT_AMB', var, 1)
        #rendered = rendered.replace('#NEUT_AMB', amb, 1)
    if mood == 'POS':
        rendered = rendered.replace('#POS_LOC', loc)
        used = []
        while '#POS_AMB' in rendered:
            var = choice(amb)
            while var in used:
                var = choice(amb)
            used.append(var)
            rendered = rendered.replace('#POS_AMB', var, 1)
        #rendered = rendered.replace('#POS_AMB', amb, 1)
    if mood == 'NEG':
        rendered = rendered.replace('#NEG_LOC', loc)
        used = []
        while '#NEG_AMB' in rendered:
            var = choice(amb)
            while var in used:
                var = choice(amb)
            used.append(var)
            rendered = rendered.replace('#NEG_AMB', var, 1)
        #rendered = rendered.replace('#NEG_AMB', amb, 1)

    rendered = render_gender(char1, rendered, char2)
    return rendered

def get_location_desc(char1, char2, location, templates):
    tmpl = get_location_template(location, templates)
    return render_location_desc(char1, char2, location, tmpl)

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
    tmpls = templates.SETTING_DESCRIPTIONS
    locations = parse.parse_locations()
    for loc in locations:
        l = locations[loc]
        tmpl = get_char_template(l, tmpls)
        if tmpl is None:
            print l
        print render_char_desc(l, tmpl)
