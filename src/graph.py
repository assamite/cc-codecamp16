'''
Graph related functionality.
'''
from random import choice

import networkx as nx

import parse

def make_graph(pairs, links=None):
    '''Make directed graph from pairs and link types.'''
    G = nx.DiGraph()
    for i, p in enumerate(pairs):
        G.add_edge(p[0], p[1], link=links[i])
    return G


def path(G, source, target):
    try: 
        p = nx.shortest_path(G, source, target)
    except:
        # Return zero path if no path is found.
        return []
    return p

def action_list(G, midpoint, initials, closings):
    nodes = G.nodes()
    if midpoint[1] not in nodes:
        raise ValueError("No such midpoint in graph")
    if midpoint[0] not in nodes:
        raise ValueError("No such midpoint before in graph")
    if midpoint[2] not in nodes:
        raise ValueError("No such midpoint after in graph")
    before = midpoint[0]
    mp = midpoint[1]
    after = midpoint [2]
    action_list = []
    starting_paths = []
    ending_paths = []
    for ini in initials:
        if ini not in nodes:
            continue
        p = nx.has_path(G, ini, before)
        if p:
            starting_paths.append(nx.shortest_path(G, ini, before))
    if len(starting_paths) == 0:
        return []

    bmp = nx.shortest_path(G, before, mp)
    amp = nx.shortest_path(G, mp, after)

    for clo in closings:
        if clo not in nodes:
            continue
        p = nx.has_path(G, after, clo)
        if p:
            ending_paths.append(nx.shortest_path(G, after, clo))
    if len(ending_paths) == 0:
        return []

    start = choice(starting_paths)
    ending = choice(ending_paths)
    return start + bmp[1:-1] + [mp] + amp[1:-1] + ending

def get_links(G, action_list):
    links = []
    for i,a in enumerate(action_list[:-1]):
        data = G.get_edge_data(a, action_list[i+1])
        
        link = data['link']
        links.append(link)
    return links

if __name__ == "__main__":
    import parse
    d = parse.parse_pairs()
    G = make_graph(d['pairs'], d['links'])
    print nx.has_path(G, 'are_marketed_by', 'take_advantage_of')
    M = parse.parse_midpoints()
    chains = M['chains']
    I = parse.parse_initials()
    initials = list(set([i[0] for i in I]))
    C = parse.parse_closings()
    closings = list(set([c[0] for c in C]))
    nodes = G.nodes()

    '''
    midb = list(set([e[0] for e in chains]))
    mida = list(set([e[2] for e in chains]))
    i = 0
    n = 0

    inits = []
    midbs = []
    for ini in initials:
        print "Ini: {}".format(ini)
        i = i + 1
        action_found = False
        for mid in midb:
            both = True
            if ini not in nodes:
                both = False
                if ini not in inits:
                    inits.append(ini)
            elif mid not in nodes:
                both = False
                if mid not in midbs:
                    midbs.append(mid)
            if both:
                p = nx.has_path(G, ini, mid)
                if p:
                    action_found = True
                    #print ini, mid
        if action_found:
            n = n + 1
    print i, n
    print inits
    print midbs
    '''
    '''
    i = 0
    n = 0
    clos = []
    midas = []
    for mid in mida:
        i = i + 1
        action_found = False
        for clo in closings:
            if mid not in nodes:
                print "Mida: {}".format(mid)
                if mid not in midas:
                    midas.append(mid)
            elif clo not in nodes:
                print "Clo: {}".format(clo)
                if clo not in clos:
                    clos.append(clo)
            else:
                p = nx.has_path(G, mid, clo)
                if p:
                    action_found = True
        if action_found:
            n = n + 1
    print i, n
    print midas
    print clos
    '''