'''
Functions for parsing the data .csv (and .xlsx) files.
'''
action_pairs_path = "../data/Veale's action pairs.csv"

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