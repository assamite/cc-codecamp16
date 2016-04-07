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

def parse_pairs(tsv_path=action_pairs_path):
    '''Parse action pairs (csv). Returns dictionary with keys 'pairs' and
    'links', which both contain a list. 'pairs' a list of two tuples (B, A),
    and 'links' is a list of strings. 
    '''
    lines = [l.strip().split("\t") for l in open(tsv_path).readlines()]
    headers, data = lines[0], lines[1:]
    dict = {}
    dict['pairs'] = [(d[1],d[3]) for d in data]
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
        b,m,a,e = d
        bs = [e.strip() for e in b.split(",")]
        ms = [e.strip() for e in m.split(",")]
        aes = [e.strip() for e in a.split(",")]
        es = tuple(e.split(":"))
        # All combinations for chains
        chains = list(itertools.product(bs,ms,aes))
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
        representations = [e.strip() for e in d[3].split(",")]
        mappings = list(itertools.product(initial, representations))
        actions = actions + mappings
    return actions


def parse_closings(tsv_path=closings_path):
    lines = [l.strip().split("\t") for l in open(tsv_path).readlines()]
    headers, data = lines[0], lines[1:]
    actions = []
    for d in data:
        initial = [d[0]]
        representations = [e.strip() for e in d[2].split(",")]
        mappings = list(itertools.product(initial, representations))
        actions = actions + mappings
    return actions


def parse_NOC(tsv_path=NOC_path):
    lines = [l.strip().split("\t") for l in open(tsv_path).readlines()]
    headers, data = lines[0], lines[1:]
    #print headers
    characters = {}
    for d in data:
        char_dict = {}
        char = d[0]
        for i in range(len(d[1:])):
            char_dict[headers[i+1]] = [e.strip() for e in d[i+1].split(",")]
        characters[char] = char_dict
    return characters

