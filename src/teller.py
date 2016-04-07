'''
Main module to put everything together.
'''
import graph
import render
import parse

from random import choice, randint

class StoryTeller():

    def __init__(self):
        self.initials = parse.parse_initials()
        self.I = list(set([i[0] for i in self.initials]))
        self.closings = parse.parse_closings()
        self.C = list(set([i[0] for i in self.closings]))
        ret = parse.parse_midpoints()
        self.midpoints = ret['chains']
        self.midpoint_ex = ret['exemplars']
        self.action_pairs = parse.parse_pairs()
        self.noc = parse.parse_NOC()
        self.exemplars = parse.parse_exemplars()
        self.action_graph = graph.make_graph(self.action_pairs['pairs'],
                                             self.action_pairs['links'])

    def tell(self, *args, **kwargs):
        '''Tell a story.
        '''
        action_list, actor1, actor2 = self.select_midpoint(*args, **kwargs)
        print action_list
        links = graph.get_links(self.action_graph, action_list)
        
        for i in range(len(action_list[:-1])):
            print "{} {} {}".format(actor1, action_list[i], actor2)
            print "{}".format(links[i])
        print "{} {} {}".format(actor1, action_list[-1], actor2)

    def select_midpoint(self, *args, **kwargs):
        '''Dummy.'''
        suitable = False
        while not suitable:
            r = randint(0, len(self.midpoints))
            midpoint = self.midpoints[r]
            ac = graph.action_list(self.action_graph, midpoint,
                                   self.I, self.C)
            if ac is not None:
                actor1, actor2 = self.select_actors(self.midpoint_ex[r])
                if actor1 is not None and actor2 is not None:
                    suitable = True
        return ac, actor1, actor2

    def select_actors(self, exemplars):
        actor1 = self.select_actor(exemplars[0])
        actor2 = self.select_actor(exemplars[1])
        while actor1 == actor2:
            actor2 = self.select_actor(exemplars[1])
        return actor1, actor2

    def select_actor(self, exemplar):
        possible_characters = []
        for char in self.exemplars:
            if exemplar in self.exemplars[char]['most']:
                possible_characters.append(char)
        if len(possible_characters) == 0:
            return None
        return choice(possible_characters)

if __name__ == "__main__":
    st = StoryTeller()
    st.tell()
    '''
    st = StoryTeller()
    ex = st.exemplars
    mex = st.midpoint_ex
    nf = 0
    for m in mex:
        m = m[0]
        not_found = True
        for k,v in ex.items():
            moste = v['most']
            for d in moste:
                if m == d:
                    not_found = False
            mleast = v['least']
            for d in mleast:
                if m == d:
                    not_found = False
        if not_found:
            print m
            nf = nf + 1
    print nf, len(mex)
    '''
    #st.tell()


