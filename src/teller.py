'''
Main module to put everything together.
'''
import graph
import render
import parse

from random import choice, randint
import re

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
        self.idiomatics = parse.parse_idiomatics()
        self.locations = parse.parse_locations()

    def tell(self, *args, **kwargs):
        '''Tell a story.
        '''

        def linearize(story, actor1, actor2):
            '''
            (1) Order elements of surface sentence.
            (2) Add punctuation to surface sentence.

            Policy for modifying references:
            * For the two opening sentences: {'opening':[(full,full), (surname,surname)]}
            * For middle sentences:
              - Any conjoined by 'and': {'CONJ_and':[(surname,surname), (ellipse,pron)]}
              - Unconjoined sentences: {'UNCONJ': [(surname,surname)]}
            * For closing sentences: {'closing':[(surname,surname)}
            * Keep a list of exception names:

            Returns dictionary with:
            * Keys: labels for each section ('opening', 'middle', 'closing')
            * Values: links & sentences, which have been linearized & punctuated
            '''
            res = {}
            comma_triggers = ['yet']
            ignore_at_sentence_start = ['and', 'but']
            sent_starters = {'so': ['for this reason', 'in spite of this', 'then'],
                            'but': ['however', 'nevertheless', 'as a reaction to this',
                                    'consequently', 'nonetheless', 'as a result',
                                    'as such', 'clearly', 'then', 'moreover', 'remarkably',
                                    'strangely', 'amazingly']}

            def alternative_refs(full_name, gender):
                refs = {}
                gender = gender[0]
                full_name = full_name[0]#TODO: only picking top item for now
                if ('the' in full_name.lower()) or (len(full_name.split(' '))<2):
                    refs['surname'] = full_name
                else:
                    refs['surname'] = full_name.split(' ')[-1]
                if gender.lower()=='male':
                    refs['prons'] = ('he', 'him')
                if gender.lower()=='female':
                    refs['prons'] = ('she', 'her')
                return refs
            actor1_can_refs_dict = alternative_refs(self.noc[actor1]['Canonical Name'], self.noc[actor1]['Gender'])
            actor2_can_refs_dict = alternative_refs(self.noc[actor2]['Canonical Name'], self.noc[actor2]['Gender'])

            #Construct opening
            opening_sents = []
            opening_link = story['opening'][0]
            opening_sentences = story['opening'][1]
            idi = choice(self.idiomatics[opening_sentences[0]])
            sentence = idi.replace('A', actor1)
            sentence = sentence.replace('B', actor2)
            opening_sents.append('{}'.format(sentence))
            if opening_link in comma_triggers:
                opening_sents.append(', {} '.format(opening_link))
            else:
                opening_sents.append(' {} '.format(opening_link))
            idi = choice(self.idiomatics[opening_sentences[1]])
            sentence = idi.replace('A', actor1_can_refs_dict['surname'])
            sentence = sentence.replace('B', actor2_can_refs_dict['surname'])
            opening_sents.append('{}. '.format(sentence))
            res['opening'] = opening_sents

            #Construct middle
            middle_sents = []
            initial_link = story['middle'][0]
            rest_middle = story['middle'][1]
            #Deal with optional initial link for middle section
            if initial_link in ignore_at_sentence_start:
                pass
            else:
                middle_sents.append('{} '.format(initial_link.capitalize()))
            #Begin formatting rest of middle section
            for n,(lnk,sent) in enumerate(rest_middle[:-1]):
                idi = choice(self.idiomatics[sent])
                sentence = idi.replace('A', actor1)
                sentence = sentence.replace('B', actor2)
                #Pick alternative sentence starter
                if lnk in sent_starters.keys():
                    alt_sent_starter = choice(sent_starters[lnk]).capitalize()
                #Skip the final link.
                if n==len(rest_middle[:-1])-1:
                    middle_sents.append("{}".format(sentence))
                    break
                middle_sents.append('{}'.format(sentence))
                if lnk in comma_triggers:
                    middle_sents.append(', {} '.format(lnk))
                elif lnk in sent_starters.keys():
                    middle_sents.append('. {}, '.format(alt_sent_starter))
                else:
                    middle_sents.append(' {} '.format(lnk))
                    #actor1_can_refs_dict['surname']
            #Deal with the final links and sentences of middle section
            middle_end_lnk = rest_middle[-1][0]
            middle_end_sent = rest_middle[-1][1]

            def finalcheck_conjoined_sents(sent_list, actr1, actr2):
                res = []
                for i in sent_list:
                    if not('.' in i) and (' and ' in i):
                        i.replace(actr1, '')
                        i.replace(actr2, actor2_can_refs_dict['prons'][1])
                        res.append(i)
                    else:
                        res.append(i)
                return res
            def finalcheck_fullnames(sent_list, actr1, actr2):
                res = []
                for i in sent_list:
                    if not('.' in i):
                        if actr1 in i:
                            i = re.sub(actr1, actor1_can_refs_dict['surname'], i)
                        if actr2 in i:
                            i = re.sub(actr2, actor2_can_refs_dict['surname'], i)
                        res.append(i)
                    else:
                        res.append(i)
                return res

            if middle_end_lnk in sent_starters.keys():
                middle_sents.append('. {}, '.format(choice(sent_starters[middle_end_lnk]).capitalize()))
                idi = choice(self.idiomatics[middle_end_sent])
                sentence = idi.replace('A', actor1)
                sentence = sentence.replace('B', actor2)
                middle_sents.append('{}. '.format(sentence))
            else:
                idi = choice(self.idiomatics[middle_end_sent])
                sentence = idi.replace('A', actor1)
                sentence = sentence.replace('B', actor2)
                middle_sents.append('. {}. '.format(sentence))

            middle_sents = finalcheck_conjoined_sents(middle_sents, actor1, actor2)
            middle_sents = finalcheck_fullnames(middle_sents, actor1, actor2)
            res['middle'] = middle_sents

            #Construct closing
            closing_sents = []
            idi = choice(self.idiomatics[story_bundle['closing']])
            sentence = idi.replace('A', actor1_can_refs_dict['surname'])
            sentence = sentence.replace('B', actor2_can_refs_dict['surname'])
            closing_sents.append('{}.'.format(sentence))
            res['closing'] = closing_sents

            return res


        plot = self.generate_plot(plots=20)
        actor1, actor2, action_list, links, evaluation = plot

        story_bundle =  {
                        'opening': (links[0], action_list[:2]),
                        'middle': (links[1],zip(links[2:-1], action_list[2:-1])),
                        'closing': action_list[-1]
                        }

        #Linearize story
        ##TODO: there's a bug where this won't work for stories of less than 4 sentences
        ##The problem is that this leads to a link being stranded at the beginning of the
        ##middle section, e.g. 'So .'
        linearized_story = linearize(story_bundle, actor1, actor2)

        #Format story
        print ''.join(linearized_story['opening'])
        print ''.join(linearized_story['middle'])
        print ''.join(linearized_story['closing'])

        #for i in range(len(action_list[:-1])):
        #    print "{} {} {}".format(actor1, action_list[i], actor2)
        #    print "{}".format(links[i])
        #print "{} {} {}".format(actor1, action_list[-1], actor2)

    def generate_plot(self, plots=100):
        '''Use generate and test-method to select best possible plot and
        character combination.
        '''
        all_plots = []
        for i in range(plots):
            action_list, actor1, actor2 = self.get_characters_and_actions()
            links = graph.get_links(self.action_graph, action_list)
            evaluation = self.evaluate_plot(actor1, actor2,
                                            action_list, links)
            all_plots.append((actor1, actor2, action_list, links, evaluation))
        all_plots.sort(key=lambda x: x[4], reverse=True)
        return all_plots[0]

    def evaluate_plot(self, actor1, actor2, action_list, links):
        return 1

    def get_characters_and_actions(self, *args, **kwargs):
        '''Dummy.'''
        suitable = False
        while not suitable:
            r = randint(0, len(self.midpoints))
            midpoint = self.midpoints[r]
            try:
                ac = graph.action_list(self.action_graph, midpoint,
                                       self.I, self.C)
            except:
                ac = None
            if ac is not None:
                actor1, actor2 = self.select_actors(self.midpoint_ex[r])
                if actor1 is not None and actor2 is not None:
                    suitable = True
        return ac, actor1, actor2

    def select_actors(self, exemplars):
        actor1 = self.select_actor(exemplars[0])
        if actor1 == None:
            return None, None
        actor2 = self.select_actor(exemplars[1])
        if actor2 == None:
            return None, None
        i = 0
        while actor1 == actor2:
            actor2 = self.select_actor(exemplars[1])
            i = i + 1
            if i >= 10:
                return None, None
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
