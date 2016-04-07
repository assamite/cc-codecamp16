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

        def linearize(story, actor1, actor2):
            '''
            (1) Order elements of surface sentence.
            (2) Add punctuation to surface sentence.
            '''
            res = ''
            comma_triggers = ['yet']
            ignore_at_sentence_start = ['and', 'but']
            sent_starters = ['so', 'but']

            #Construct opening
            opening_link1 = story['opening'][0][0]
            opening_link2 = story['opening'][0][1]
            opening_sentences = story['opening'][1]
            res = '{} {} {}'.format(actor1, opening_sentences[0], actor2)
            if opening_link1 in comma_triggers:
                res = res+', {} '.format(opening_link1)
            else:
                res = res+' {} '.format(opening_link1)
            res = res+'{} {} {}. '.format(actor1, opening_sentences[1], actor2)
            if opening_link2 in ignore_at_sentence_start:
                pass
            else:
                res = res+'{} '.format(opening_link2.capitalize())

            #Construct middle
            for n,(lnk,sent) in enumerate(story['middle'][:-1]):
                #Skip the final link.
                if n==len(story['middle'][:-1])-1:
                    res = res+"{} {} {}".format(actor1, sent, actor2)
                    break
                res = res+"{} {} {}".format(actor1, sent, actor2)
                if lnk in comma_triggers:
                    res = res+', {} '.format(lnk)
                elif lnk in sent_starters:
                    res = res+'. {} '.format(lnk.capitalize())
                else:
                    res = res+' {} '.format(lnk)
            middle_end_lnk = story['middle'][-1][0]
            middle_end_sent = story['middle'][-1][1]
            if middle_end_lnk in sent_starters:
                res = res+'. {} '.format(middle_end_lnk.capitalize())
                res = res+'{} {} {}. '.format(actor1, middle_end_sent, actor2)
            else:
                res = res+'. {} {} {}. '.format(actor1, middle_end_sent, actor2)

            #Construct closing
            res = res+'{} {} {}.'.format(actor1, story_bundle['closing'], actor2)

            return res


        action_list, actor1, actor2 = self.select_midpoint(*args, **kwargs)
        print action_list
        links = graph.get_links(self.action_graph, action_list)

        story_bundle =  {
                        'opening': (links[0:2], action_list[:2]),
                        'middle': zip(links[2:-1], action_list[2:-1]),
                        'closing': action_list[-1]
                        }

        print linearize(story_bundle, actor1, actor2)
        
        #for i in range(len(action_list[:-1])):
        #    print "{} {} {}".format(actor1, action_list[i], actor2)
        #    print "{}".format(links[i])
        #print "{} {} {}".format(actor1, action_list[-1], actor2)

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
