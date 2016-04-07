'''
Templates for different types of sentences.

#NAME = name of the character
#GPR = gender pronoun
#POS = positive talking point or trait
#NEG = negative talking point or trait
#POS_ADJ =
'''
GPR = {'male': 'he', 'female': 'she'}

POS_ADJ = [
    "great",
    "smart",
    ]


CHARACTER_DESCRIPTIONS = [
    "#NAME was #POS as #GPR was #POS.",
    "#NAME was #NEG as #GPR was #NEG.",
    ""
    ]

PAIRS_BUT = [
    "#ACTOR1 #VERB1 #ACTOR2, but "
    ]