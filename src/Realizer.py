#encoding=utf8
"""
Module for handling surface realization.

Input: string to change
Output: changed string

"""

from pattern.en import tag, conjugate, PAST


class Realizer(object):

    def __init__(self):
        pass

    def simplepastify_action_pairs(self, action_string):
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

        for i in action_string.split('_'):
            res.append(process(i))
        return  '_'.join('%s' % r for r in res)


if __name__ == '__main__':

    action_pairs_string = parse_pairs(action_pairs_path)['pairs'][10][1]
    print Realizer().simplepastify_action_pairs(action_pairs_string)
