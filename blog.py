# Generate the monthly 2600 web page
import datetime
import calendar
import sys
import os

PRESENTATIONS = './presentations.txt'
with open(PRESENTATIONS) as fp:
    preslist = "\n\n" + fp.read()

if len(sys.argv) > 1:
    OUTPUT = sys.argv[1]
    assert os.path.isdir(OUTPUT)
else:
    OUTPUT = None




def generate_output(meeting_date, edition, image):
  global OUTPUT
  text = []
  text.append("+"*3)
  text.append("title =  \"Meeting %s %s Edition\"" % ( meeting_date, edition))
  text.append("date = \"%s\"" % datetime.datetime.today().strftime('%Y-%m-%d'))
  text.append("type = \"post\"")
  text.append("author = \"antitree\"")
  text.append("+"*3)
  text.append("")
  text.append('[![2600](/images/2600_%s.png)](images/2600_%s.png)' % (image, image))
  text.append("")
  text.append(chomsky())
  if OUTPUT:
	  f = open("%s/%s.md" % (OUTPUT, datetime.datetime.today().strftime('%m-%d-%Y')), 'w')
	  f.writelines("%s\n" % t for t in text)
  else:
	  for line in text:
		  print(line)


# List of LEADINs to buy time.
leadins = """Join us this month for a
	Attending a 2600 meeting this month means you will see a
	The First Friday 2600 meeting will be a
	2600 this month is a
	Get ready for a
	Wow. Big month. It'll be a
	Rochester 2600 is going to devote some time to be a
	For thos interested, the meeting this month is a
        Welp. Time for another meeting. Come on down this month and see a"""

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
        metric fuck-ton of
        speed round about
        unadulturated look at
        existential look at
        confusing explanation of
        a very serious discussion about
        a solumn discussion of
	deep dive into"""

# List of SUBJECTs chosen for maximum professorial macho.
subjects = """docker
	Jason's dark secrets
	information security
	humanity
	religion
        alcoholism
        climate change
        primates
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
        Donald Trump
        Donald Trump's hair
        security
        hacking
        power lifting
        bro science
        compassion and empathy
        safety
        risk management
        the color purple
        meth
        club mate
        gymnastics
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
        while we listen to
	while we sip our drinks and look at"""


# List of OBJECTs selected for profound sententiousness.

objects = """ problems of
        a corpus of utterance tokens between
        a sumo wrestle match between
        a size comparison of
	the differences between
	documented gender barriers of
	an oversimplified comparative anlaysis of
	the effects ridilin has on
	which melts faster between
	implications of nostril hair on
        an analysis of
        a risk analysis of
        a deep look at
        a somber discussion of
        common methods of destroying
        the strength of
        a deeply sad comparison between
        a parasitic gap construction."""

pobj = """ Dan Kaminski
	Jason Ross
	a pound of butter
	right-wing squirrels
	power hungry dwarves
	Shmoocon
	DEFCON
	nose hair
	eye brows
	Denny's Moons Of My Hammy
	a depressed fourth grader
	Thomas
	Joe
	Bill
	AntiTree
	Andrew
	the cast of Glee
	that weird guy that comes in sometimes
	cryptography
	T.O.R.
	two fluffy pillows
	MongoDB
	JSON
	python
	go-lang
	Java
	NodeJS
	Bitcoin
	Ethereium
	ZCash
        Brian
        Tupac
        Biggy Smalls
        a flock of angry seaguls
        pseudoscience
        climate change
        attack helicopters
        brave 4th graders
        hungry 8th graders
        depressed goth kids
        crippling depression
        Rochester
        Penfield
        Chicago
        Washington
        lean beef
        meatloaf
        gibberish
        gouls
        competitive urinating
        demons
        angels
        Rust
        headphones
        people with huge heads
        books
        Jason's lost soul
        a primary school teacher
        1973 Chevy Nova
        hate
        feelings
        anger
        fear
        regret
        crippiling regret
        anxiety
        powerful emotions
        predictive crystals
        mobile
        cloud
        cyber clouds
        cyber
        mobile cybers
        8 pounds of monkey limbs
        radios
        SDR
        cell towers
	balls"""

bobj = """ and
	and"""


presentations = """Presentations this months include:
	This will be done via presentations below:
	Here is an agenda for the night:
	Here's what you can expect:
	Well here it is:
	Anyways, here's the list of talks:
	Gah. Whatever. Talks below:
	YOLO:
	I appologize in advance for the following talks:
        Here are the actual talks this month:
        Ok. J/K, here are the talks:
        These are actually the talks we have scheduled:
	Agenda below:"""

disclaimer = """NOTE: This page was generated by the 2600 blog generator bot. While the presentations are true, nothing else is
	[generated by the sacastic 2600 bot of doom]
	Disclaimer: All blog text is automatically generated by the 2600 bot of doom. We do not really know what will be produced. All complaints should be directed at the bot and not Andrew."""


import textwrap, random
from itertools import chain, islice, izip
from time import sleep

def chomsky(times=1, line_length=72):
    parts = []
    for part in (leadins, descriptions, subjects, verbs, objects, pobj, bobj, pobj,""".""", presentations):
        phraselist = map(str.strip, part.splitlines())  # !3
        random.shuffle(phraselist)
        parts.append(phraselist)
    output = chain(*islice(izip(*parts), 0, times))   # !3
    return textwrap.fill(' '.join(output), line_length) + preslist  # !3

def first_friday_finder(year, month):
	#find next first friday
    c = calendar.Calendar(firstweekday=calendar.SUNDAY)
    monthcal = c.monthdatescalendar(year, month)
    return [day for week in monthcal for day in week if day.weekday() == calendar.FRIDAY and day.month == month][0]

today = datetime.datetime.today()
ff = first_friday_finder(today.year, today.month)
if (ff - datetime.date.today()).days < 0:
    ff = first_friday_finder(today.year, today.month + 1)
ff = ff.strftime('%m/%d/%Y')

meeting_date = raw_input("What's the date of the next meeting? (%s)" % ff) or ff
edition = raw_input("What's the edition? (e.g. Trump, Black Santa): ")
image = raw_input("What's the name alone of the image? (%s): " % edition.lower()) or edition.lower()
generate_output(meeting_date, edition, image)
