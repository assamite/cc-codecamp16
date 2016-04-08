'''
Templates for different types of sentences.

#NAME = name of the character
#NOM = name of second character
#GPR = gender pronoun
#POS = positive talking point or trait
#NEG = negative talking point or trait
#GNN = gender noun
#PNR = Gender reflexive pronoun 
#GPN = Gender possessive pronoun
#NOP = Second person gender pronoun
#LOC = setting/location
#DET = determiner
#AMB = ambience
#PREP = preposition 
#POS_LOC = a more positive, pleasant location
#NEG_LOC = a more negative location
#POS_AMB = an ambience that goes with a positive location
#NEG_AMB = an ambience that goes with a negative location
#NEUT_LOC = a location with both positive and negative aspects
#NEUT_AMB = ambient words that can be negative or positive or neutral

Possible differentiation of positive and negative settings in order to have
character reactions and thoughts that make sense in terms of them.
'''
GPR = {'male': 'he', 'female': 'she'}
NOP = {'male': 'he', 'female': 'she'}
GNN = {'male': 'man', 'female': 'woman'}
PNR = {'male': 'himself', 'female': 'herself'}
GPN = {'male': 'his', 'female': 'her'}
GPS = {'male': 'him', 'female': 'her'}

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
    "#NAME was as #POS as #GPR was #POS.",
    "#NAME was as #NEG as #GPR was #NEG.",
    "#NOM was as #NEG as #GPR was #NEG.",
    "#NOM was as #POS as #GPR was #POS.",
    "#NAME was as #NEG as #GPR was #POS.",
    "#NAME was as #POS as #GPR was #NEG.",
    "#NOM was as #NEG as #GPR was #POS.",
    "#NOM was as #POS as #GPR was #NEG.",
    "#NAME was as #POS as #NOM was #NEG.",
    "#NOM was as #POS as #NAME was #NEG.",
    "#NAME, a #POS and #POS #GNN, had a knack for getting people to do things.",
    "#NAME, as a #NEG #GNN, often got what #GPR wanted.",
    "A #POS #GNN, #NAME was widely respected in #GPN social circles.",
    "Even #NAME's closest acquaintances steered clear of #GPS because they knew what a #NEG #GNN #GPR was.",
    "#NAME, who appeared #POS and #POS, occasionally slipped up and let people see #GPN #NEG side.",
    "#NOM wanted people to think #GPR was only #NEG and #NEG. If people found out #GPR was also #POS, they would never look at #GPR the same.",
    "A #POS and #POS #GNN, #NAME was well-liked.",
    "Everyone thought #NAME was such a #POS #GNN, but #GPR was quite #NEG as well.",
    "A #NEG and #NEG #GNN, #NAME was not well-liked.",
    "People admired #NAME for #GPN #POS personality.",
    "People didn't like #NAME because of #GPN #NEG character.",
    "#NOM was envious of how #POS #NAME was."
    "#NAME never understood why #NOM was so #NEG.",
    "Some people wouldn't like to be #NEG or #NEG, but #NOM embraced these qualities in #PNR.",
    ]

CHARACTER_RELATIONSHIPS = [
    "#NOM wondered how #NAME came to be such a #NEG and #NEG person.",
    "#NOM always looked up to #NAME for #GPR #POS personality."
    ]

ACTION_PAIRS_BUT = [
    '#NAME #ACT #2NAME, but #GPR #2ACT #2NAME.',
#    'As #PADJ as #NAME was #GPR #ACT #2NAME, but realizing what #GPR had '+
#    ' done #GPR #2ACT #2NAME.',
    ]

ACTION_PAIRS_AND = [
    '#NAME #ACT #2NAME, and #GPR #2ACT #2NAME.',
    ]

ACTION_PAIRS_BECAUSE = [
    '#NAME #ACT #2NAME, because #NAME #2ACT #2NAME.',
    ]

ACTION_PAIRS_YET = [
    '#NAME #ACT #2NAME, yet #NAME #2ACT #2NAME.',
    ]

ACTION_PAIRS_SO = [
    '#NAME #ACT #2NAME, so #NAME #2ACT #2NAME.',
    ]

SETTING_DESCRIPTIONS = [
    "#PREP the #NEUT_AMB #NEUT_LOC, #NAME waited for #NOM. #GPR knew #NOM would be coming, because #NOP always came at this time.",
    "#NAME looked around the #NEG_AMB #NEG_LOC, wondering how #GPR had ended up here.",
    "#NAME looked around the #NEUT_AMB #NEUT_LOC, wondering how #GPR had ended up here.",
    "#NAME looked around the #POS_AMB #POS_LOC, wondering how #GPR had ended up here.",
    "The #POS_LOC was #POS_AMB and #POS_AMB, causing a smile to light #NAME's face.",
    "#NAME began to feel weary while looking around the #NEG_AMB, #NEG_AMB #NEG_LOC.",
    "Excitement coursed through #NAME's veins as #GPR entered the #POS_LOC.",
    "Fear coursed through #NAME's veins as #GPR entered the #NEG_LOC.",
    "The #NEG_AMB and #NEG_AMB of the #NEG_LOC made #NAME's knees shake, but #GPR couldn't show fear.",
    "#NAME examined #GPN surroundings with an air of indifference. The #NEUT_AMB state of the #NEUT_LOC was neither welcoming nor excluding.",
    "AS #NAME entered the #POS_LOC, #GPR was struck by the sound of children's laughter filling the air.",
    "The #NEG_AMB #NEG_LOC made #NAME uncomfortable, but #GPR had no option but to stay there.",
    "The #POS_LOC always reminded #NAME of home because of how #POS_AMB and #POS_AMB it was.",
    "The #NEG_LOC #NAME found #PNR in was #NEG_AMB and #NEG_AMB.",
    "The #POS_LOC #NAME found #PNR in was #POS_AMB and #POS_AMB.",
    "#NAME quite liked the #POS_AMB #POS_LOC and frequented as often #GPR could",
    "#NOM hated #NEG_AMB #NEG_LOC s like the  one #NOP currently found #PNR in.",
    "#NAME walked confidently through the #AMB #LOC.",
    "It was late in the evening when #NAME found #PNR in a #NEUT_AMB #NEUT_LOC.",
    "It was late in the evening when #NAME found #PNR in a #NEG_AMB #NEG_LOC.",
    "It was late in the evening when #NAME found #PNR in a #POS_AMB #POS_LOC.",
    "In the late evening, #NAME found #PNR in a #NEUT_AMB #NEUT_LOC.",
    "In the late evening, #NAME found #PNR in a #NEG_AMB #NEG_LOC.",
    "In the late evening, #NAME found #PNR in a #POS_AMB #POS_LOC.",
    "In the late evening, #NAME encountered #NOM in a #NEUT_AMB #NEUT_LOC.",
    "In the late evening, #NAME encountered #NOM in a #NEG_AMB #NEG_LOC.",
    "In the late evening, #NAME encountered #NOM in a #POS_AMB #POS_LOC.",
    "The #NEUT_LOC was #NEUT_AMB and #NEUT_AMB.",
    "In the early morning, people trickled #PREP #DET #POS_LOC. It was #POS_AMB and #POS_AMB.",
    "Many people avoided the #NEG_LOC, no one wanted to spend time there.",
    "The #NEG_LOC was #NEG_AMB and #NEG_AMB.",
    "The #POS_LOC was #POS_AMB and #POS_AMB.",
    "Of all the places #NAME expected to find #NOM, #DET #POS_LOC was not one of them.",
    "Of all the places #NAME expected to find #NOM, #DET #NEG_LOC was not one of them.",
    "Of all the places #NAME expected to find #NOM, #DET #NEUT_LOC was not one of them.",
    "#NAME wasn't fond on #NEG_AMB places, like the #NEG_LOC #GPR was currently in.",
    "#NAME glanced around, appreciating the #POS_AMB quality of the #POS_LOC #GPR was currently in.",
    ]

PAIRS_BUT = [
    "#ACTOR1 #VERB1 #ACTOR2, but "
    ]
