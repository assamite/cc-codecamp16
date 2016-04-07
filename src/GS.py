#encoding=utf8
"""
Module for interfacing with Gensim.

USAGE:
    * Place model, e.g. 'w2v_103.model' in the 'data' directory.
    * Also see example at bottom of this file.

For general gensim info, go here:
* http://radimrehurek.com/2013/09/deep-learning-with-word2vec-and-gensim/

To train the models, check the information on this page:
* https://code.google.com/p/word2vec/
** In particular, check the sections "Where to obtain the training data", "Pre-trained word and phrase vectors", etc
The simplest approach is to download the following pre-processed data set locally:
* http://www.statmt.org/lm-benchmark/1-billion-word-language-modeling-benchmark-r13output.tar.gz

"""

import os, re

import numpy as np
from gensim.models import Word2Vec

# Some useful variables
pthsplit = os.path.split
pthjoin = os.path.join
listdir = os.listdir
isfile = os.path.isfile
write = os.write


class GS(object):

    def __init__(self, loaded_model):
        self.LOADED_MODEL = loaded_model

    def sim_score_stringlists(self, stringlist1, stringlist2):
        """
        params:
        :stringlist1: Space separated list of words
        :stringlist2: Space separated list of words
        :trained_model: supplied when initialising GS

        returns similarity score for
        """

        def uncontract(s):
            res = ""
            if "n't" in s:
                res = s[0:-3]+" not"
            elif "'m" in s:
                res = s[0:-2]+" am"
            else:
                res = s
            return res

        #Pre-process each of the strings
        ##String set 1
        strl1 = ''.join(utt.lower() for utt in stringlist1 if utt)
        strl1 = re.sub("[;':)(=’]", '', strl1)
        ##String set 2
        strl2 = ''.join(utt.lower() for utt in stringlist2 if utt)
        strl2 = re.sub("[;':)(=’]", '', strl2)

        strl1 = [s for s in strl1.split(' ') if s in self.LOADED_MODEL.vocab]
        strl2 = [s for s in strl2.split(' ') if s in self.LOADED_MODEL.vocab]

        try:
            return self.LOADED_MODEL.n_similarity(strl1, strl2)
        except KeyError as e:
            print "Getting error: ",e," -- when checking similarity between:"
            print "List 1:",strl1
            print "List 2:",strl2
            return np.NaN


if __name__ == '__main__':

    print 'Loading model...'
    PATH_TO_MODEL = 'PATH\\TO\\MODEL'
    loaded_model = Word2Vec.load(PATH_TO_MODEL)
    gensim_model = GS(loaded_model)
    print 'Model loaded.'

    str1 = 'Batman goes to Disney Land.'
    str2 = 'Donald Duck goes to Gotham.'
    print gensim_model.sim_score(str1, str2)
