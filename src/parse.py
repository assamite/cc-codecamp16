'''
Functions for parsing the data .csv (and .xlsx) files.
'''
import itertools
from yaml.events import MappingStartEvent

action_pairs_path = "../data/Veale's action pairs.csv"
midpoints_path = "../data/Veale's script midpoints.csv"
initials_path = "../data/Veale's initial bookend actions.csv"
closings_path = "../data/Veale's closing bookend actions.csv"
NOC_path = "../data/Veale's The NOC List.csv"
exemplars_path = "../data/character_typical_exemplars_2.tsv"
locations_path = "../data/Veale's location listing.csv"
idiomatics_path = "../data/Veale's idiomatic actions.csv"
character_properties_path = "../data/character_properties.tsv"


def parse_pairs(tsv_path=action_pairs_path):
    '''Parse action pairs (csv). Returns dictionary with keys 'pairs' and
    'links', which both contain a list. 'pairs' a list of two tuples (B, A),
    and 'links' is a list of strings. 
    '''
    lines = [l.strip().split("\t") for l in open(tsv_path).readlines()]
    headers, data = lines[0], lines[1:]
    dict = {}
    dict['pairs'] = [(d[1], d[3]) for d in data]
    dict['links'] = [d[2] for d in data]
    return dict


def parse_midpoints(tsv_path=midpoints_path):
    '''Parse script midpoints (csv). Returns dictionary with keys 'chains' and
    'exemplars', which both contain a list. 'chains' a list of three tuples
    (before, midpoints, after), and 'exemplars' is a list of two tuples for
    exemplar actors A and B. 
    '''
    lines = [l.strip().split("\t") for l in open(tsv_path).readlines()]
    headers, data = lines[0], lines[1:]
    dict = {}
    dict['chains'] = []
    dict['exemplars'] = []
    for d in data:
        b, m, a, f = d
        bs = [e.strip() for e in b.strip().split(",") if len(e) > 0]
        ms = [e.strip() for e in m.strip().split(",") if len(e) > 0]
        al = [e.strip() for e in a.strip().split(",") if len(e) > 0]
        es = tuple(f.strip().split(":"))
        # All combinations for chains
        chains = list(itertools.product(bs, ms, al))
        for c in chains:
            dict['chains'].append(c)
            dict['exemplars'].append(es)
    return dict


def parse_initials(tsv_path=initials_path):
    lines = [l.strip().split("\t") for l in open(tsv_path).readlines()]
    headers, data = lines[0], lines[1:]
    actions = []
    for d in data:
        initial = [d[0]]
        representations = [e.strip() for e in d[3].split(",") if len(e) > 0]
        mappings = list(itertools.product(initial, representations))
        actions = actions + mappings
    return actions


def parse_closings(tsv_path=closings_path):
    lines = [l.strip("\n").split("\t") for l in open(tsv_path).readlines()]
    # After line 244 the closings are not in the same format.
    headers, data = lines[0], lines[1:244]
    actions = []
    for d in data:
        if len(d) != 3:
            continue
        closing = [d[0]]
        representations = [e.strip() for e in d[2].split(",") if len(e) > 0]
        mappings = list(itertools.product(closing, representations))
        actions = actions + mappings
    return actions


def parse_NOC(tsv_path=NOC_path):
    lines = [l.strip("\n").split("\t") for l in open(tsv_path).readlines()]
    headers, data = lines[0], lines[1:]
    # print headers
    characters = {}
    for d in data:
        char_dict = {"Character": [],
                     "Canonical Name": [],
                     "Gender": [],
                     "Address 1": [],
                     "Address 2": [],
                     "Address 3": [],
                     "Politics": [],
                     "Marital Status": [],
                     "Opponent": [],
                     "Typical Activity": [],
                     "Vehicle of Choice": [],
                     "Weapon of Choice": [],
                     "Seen Wearing": [],
                     "Domains": [],
                     # Genres    Fictive Status    Portrayed By    Creator    Creation    Group Affiliation    Fictional World    Category
                     'Negative Talking Points': [],
                     "Positive Talking Points": [],
                     }
        char = d[0]
        for i in range(len(d)):
            char_dict[headers[i]] = [e.strip() for e in d[i].split(",") if len(e) > 0]
        characters[char] = char_dict
    return characters


def parse_exemplars(tsv_path=exemplars_path):
    lines = [l.strip("\n").split("\t") for l in open(tsv_path).readlines()]
    data = lines
    characters = {}
    for d in data:
        characters[d[0]] = {}
        characters[d[0]]['most'] = [e.strip().lower() for e in d[1].split(",") if len(e) > 0]
        characters[d[0]]['least'] = [e.strip().lower() for e in d[2].split(",") if len(e) > 0]
    return characters


def parse_character_properties(tsv_path=character_properties_path):
    lines = [l.strip("\n").split("\t") for l in open(tsv_path).readlines()]
    data = lines
    characters = {}
    for d in data:
        characters[d[0]] = [tuple(e.strip().lower().split(':')) for e in d[1].split(",") if len(e) > 0]
    return characters


def parse_idiomatics(tsv_path=idiomatics_path):
    lines = [l.strip("\n").split("\t") for l in open(tsv_path).readlines()]
    headers, data = lines[0], lines[1:]
    actions = {}
    for d in data:
        action = d[0]
        idiomatics = [e.strip() for e in d[3].split(",") if len(e) > 0]
        actions[action] = idiomatics
    return actions


def parse_locations(tsv_path=locations_path):
    lines = [l.strip("\n").split("\t") for l in open(tsv_path).readlines()]
    headers, data = lines[0], lines[1:]
    locations = {}
    for d in data:
        loc = {'Location': '',
               'Mood': '',
               'Determiner': '',
               'Preposition': '',
               'Ambience': []
               }
        key = d[0]
        for i in range(len(d)):
            splitted = d[i].split(",")
            if len(splitted) == 1:
                loc[headers[i]] = splitted[0].strip()
            else:
                loc[headers[i]] = [e.strip() for e in splitted if len(e) > 0]
        locations[key] = loc
    return locations
