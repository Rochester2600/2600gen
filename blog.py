# Generate the monthly 2600 web page

PRESENTATIONS = './presentations.txt'
with open(PRESENTATIONS) as fp:
	preslist = "\n\n" + fp.read()

# List of LEADINs to buy time.
leadins = """Join us this month for a
	Attending a 2600 meeting this month means you will see a
	The First Friday 2600 meeting will be a
	2600 this month is a
	Get ready for a
	For thos interested, the meeting this month is a"""

descriptions = """trist into
	celebration of
	exploration of
	hilarious examination of
	cornicopia of
	giant pile of
	slap in the face of
	time for awkward lack of eye contact as we chat about
	time for us all to think about
	eye-brow raising thought exercise about
	balls deep discussion of
	trist into
	YOLO! exclamation about
	deep dive into"""

# List of SUBJECTs chosen for maximum professorial macho.
subjects = """docker
	Jason's dark secrets
	information security
	humanity
	religion
	the question of life
	politics and beer
	beer and whiskey
	scotch and sadness
	unholy matrimonies
	tired llamas
	why Thomas is here
	JP Bourget"""

subjects = """our deepest desires
	pride and prejudice
	racism and white people
	gender balance
	politics
	dogs
	our feelings
	depression
	happiness
	prestigue
	power
	money
	hacking
	security
	mother/daughter relationships
	dissapointment
	the state of infosec
	privacy
	anonymity
	the separation of church and state
	monkeys and their relationships
	the information divide
	alternative currencies
	balls
	Dick Cheney
	George Bush
	pure unadulterated ignorance
	unmitigated hate"""

#List of VERBs chosen for autorecursive obfuscation.
verbs = """while we take a look at
        as we explore
	while we watch
	as we dive head first into
	while we open up the forums to discuss
	as we put in just the tip about
	as we complain about
	and its negative affect on the economy and talk about
	as we drink the pain away about
	as we ask ourselves - who dat - and think about
	as we put our ear to the ground about
	during which time we check out
	in spite of our discussion about
	throughout our meditation on
	in spite of our presenters disclosing their feelings on
	much as our presenters share their knoweldge about
	as we appologize for
	while we sip our drinks and look at"""


# List of OBJECTs selected for profound sententiousness.

objects = """ problems of phonemic and morphological analysis.
        a corpus of utterance tokens upon which conformity has been defined by the paired utterance test.
        the traditional practice of grammarians.
        the levels of acceptability from fairly high (e.g. (99a)) to virtual gibberish (e.g. (98d)).
        a stipulation to place the constructions into these various categories.
        a descriptive fact.
        a parasitic gap construction."""

presentations = """Presentations this months include:
	This will be done via presentations below:
	Here is an agenda for the night:
	Here's what you can expect:
	Well here it is:
	Anyways, here's the list of talks:
	Gah. Whatever. Talks below:
	YOLO:
	I appologize in advance for the following talks:
	Agenda below:"""

import textwrap, random
from itertools import chain, islice, izip
from time import sleep

def chomsky(times=1, line_length=72):
    parts = []
    for part in (leadins, descriptions, subjects, verbs, objects, presentations):
        phraselist = map(str.strip, part.splitlines())
        random.shuffle(phraselist)
        parts.append(phraselist)
    output = chain(*islice(izip(*parts), 0, times))
    return textwrap.fill(' '.join(output), line_length) + preslist

print chomsky()



