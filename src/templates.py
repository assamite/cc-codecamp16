'''
Templates for different types of sentences.

#NAME = name of the character
#NAME2 = name of second character
#GPR = gender pronoun
#POS = positive talking point or trait
#NEG = negative talking point or trait
#GNN = gender noun
#PNR = Gender reflexive pronoun 
#LOC = setting/location
#DET = determiner
#AMB = ambience
#PREP = preposition 
#POS_LOC = a more positive, pleasant location
#NEG_LOC = a more negative location
#POS_AMB = an ambience that goes with a positive location
#NEG_AMB = an ambience that goes with a negative location

Possible differentiation of positive and negative settings in order to have
character reactions and thoughts that make sense in terms of them.
'''
GPR = {'male': 'he', 'female': 'she'}
GNN = {'male': 'man', 'female': 'woman'}
PNR = {'male': 'himself', 'female': 'herself'}

POS = [
    "great",
    "smart",
    "cunning",
    "kind",
    "amiable",
    "brilliant",
    "aspiring",
    "articulate",
    "compassionate",
    "confident",
    "cultured",
    "creative",
    "innovative",
    "dedicated",
    "dignified",
    "dutiful",
    "elegant",
    "freethinking",
    "gallant",
    "flexible",
    "focused",
    "multi-faceted",
    "open",
    "meticulous",
    "peaceful",
    "practical",
    "scrupulous",
    "strong",
    "trustful",
    "upright",
    "venturesome",
    "wise",
    "witty",
    "suave",
    "steadfast",
    "respectful",
    "responsible",
    "principled",
    "patient",
    "insouciant",
    "humble",
    "generous",
    "gentle",
    "adaptive",
    "articulate",
    "clever",
    ]

NEG = [
    "sloppy",
    "mean",
    "forceful",
    "prideful",
    "blunt",
    "brutal",
    "calculating",
    "careless",
    "childish",
    "conceited",
    "fearful",
    "foolish",
    "gloomy",
    "graceless",
    "mawkish",
    "stingy",
    "negligent", 
    "moody",
    "offhand",
    "furtive",
    "opinionated",
    "paranoid",
    "presumptuous",
    "reactive",
    "repressed",
    "resentful",
    "scornful",
    "single-minded",
    "superficial",
    "superstitious",
    "tactless",
    "tasteless",
    "oppressive",
    "domineering", 
    "venomous",
    "unloveable",
    "troublesome",
    "thoughtless",
    "strong-willed",
    "self-indulgent",
    "fickle",
    "erratic",
    "dissolute",
    "discourteous",
    "dishonest",
    "destructive",
    "demanding",
    "cruel",
    "crude",
    "aloof",
    "assertive",
    "asocial",
    "apathetic",
    "barbaric",
    "arrogant", 
    "authoritarian", 
    ]

CHARACTER_DESCRIPTIONS = [
    "#NAME was #POS as #GPR was #POS.",
    "#NAME was #NEG as #GPR was #NEG.",
    "#NAME, a #POS and #POS #GNN, had a knack for getting people to do things.",
    "#NAME, as a #NEG #GNN, often got what #GPR wanted.",
    "A #POS #GNN, #NAME was widely respected in #GPR social circles.",
    "Even #NAME’s closest acquaintances steered clear of #GPR because they knew what a #NEG #GNN #GPR was.",
    "#NAME, who appeared #POS and #POS, occasionally slipped up and let people see #GPR #NEG side.",
    ]

CHARACTER_RELATIONSHIPS = [
    "#NAME2 wondered how #NAME came to be such a #NEG and #NEG person.",
    "#NAME2 always looked up to #NAME for #GPR #POS personality."
    ]

SETTING_DESCRIPTIONS = [
    "#PREP #DET #AMB #LOC, #NAME waited for #NAME2. #GPR knew #NAME2 would be coming, because #GPR always came at this time.",
    "#Name looked around the #NEG_AMB #LOC, wondering how #GPR had ended up here.",
    "The #POS_LOC was #POS_AMB and #POS_AMB, causing a smile to light #NAME’s face.",
    "#NAME began to feel weary while looking around the #NEG_AMB, #NEG_AMB #NEG_LOC.",
    "AS #NAME entered the #POS_LOC, #GPR was struck by the sound of children’s laughter filling the air.",
    "The #NEG_AMB #NEG_LOC made #NAME uncomfortable, but #GPR had no option but to stay there.",
    "The #POS_LOC always reminded #NAME of home because of how #POS_AMB and #POS_AMB it was.",
    "The #NEG_LOC #NAME found #PNR in was #NEG_AMB and #NEG_AMB.",
    "#NAME2 hated #NEG_AMB #NEG_LOC s like the  one #GPR currently found #PNR in.",
    "#NAME walked confidently through the #AMB #LOC.",
    "It was late in the evening when #NAME found #PNR in a #AMB #LOC.",
    ]
#How do you pluralize locations?
PAIRS_BUT = [
    "#ACTOR1 #VERB1 #ACTOR2, but "
    ]
