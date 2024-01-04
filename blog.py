# Generate the monthly 2600 web page
import datetime
import calendar
import sys
import os
from shutil import copyfile

PRESENTATIONS = './presentations.txt'
DEFAULT_OUTPUT_DIRECTORY = '../rochester2600-hugo'
DEFAULT_MEETUP_GROUP = 'https://www.meetup.com/Interlock-Rochester-Hackerspace/'
DEFAULT_FACEBOOK_GROUP = 'https://www.facebook.com/groups/rochester2600/events/'
DEFAULT_LOCATION = 'Global Cybersecurity Institute at RIT'
DEFAULT_LOCATION_LINK = 'https://www.google.com/maps/place/RIT+Global+Cybersecurity+Institute/@43.0837456,-77.6831996,17z/data=!4m5!3m4!1s0x89d14d2c49d8c867:0x334b947e3eed5a20!8m2!3d43.0837456!4d-77.6810109'
with open(PRESENTATIONS) as fp:
    preslist = "\n\n" + fp.read()

if len(sys.argv) > 1:
    OUTPUT = sys.argv[1]
    assert os.path.isdir(OUTPUT)
else:
    print("Output directory not set. Should I just use %s?" % DEFAULT_OUTPUT_DIRECTORY)
    sufficient = input("(Y/n) ") or "y"
    if sufficient.lower() == "y": 
        OUTPUT = DEFAULT_OUTPUT_DIRECTORY
    else: 
        OUTPUT = None

if OUTPUT:
    OUTPUT_CONTENT = OUTPUT + '/content/meetings'
    OUTPUT_IMAGES = OUTPUT + '/static/images'
    assert os.path.isdir(OUTPUT_CONTENT)
    assert os.path.isdir(OUTPUT_IMAGES)


# List of LEADINs to buy time.
leadins = """Join us this month for a
	Attending a 2600 meeting this month means you will see a
	The First Friday 2600 meeting will be a
	2600 this month is a
	Get ready for a
	Wow. Big month. It'll be a
	Rochester 2600 is going to devote some time to be a
	For those interested, the meeting this month is a
        It's the First Friday of the month. You know what that means. It's a 2600 meeting! This month is a
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
	trist into
	YOLO! exclamation about
        metric fuck-ton of
        speed round about
        unadulturated look at
        existential look at
        confusing explanation of
        sarcastic discussion of
        powerful discussion of
        very serious discussion about
        solumn discussion of
        AI driven
        automated discussion
	deep dive into"""

# List of SUBJECTs chosen for maximum professorial macho.
subjects = """docker
        Mormonism
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
        why Jason isn't here
        posers
        scenesters
        pentesting monkeys
        emotional intelligence
    eBPF 
    NFTs
    cryptozoology
    symantec antivirus
    crypto-bros
	"""

subjects = """our deepest desires
	pride and prejudice
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
        polo shirts
        red solo cups
        posers
        scenesters
	pure unadulterated ignorance
        why Jason hasn't showed up
	unmitigated hate"""

#List of VERBs chosen for autorecursive obfuscation.
verbs = """while we take a look at
        as we explore
	while we watch
	as we dive head first into
	while we open up the forums to discuss
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
	while we sip our drinks and look at
    while we make sure not to make eye contact with"""


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
        femtocells
        cell towers
        eBPF programs"""

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

disclaimer = """Disclaimer: All blog text is automatically generated by the 2600 bot of doom. The presentations are real but otherwise we do not really know what will be produced. All complaints should be directed at the bot."""


import textwrap, random
from itertools import chain, islice
from time import sleep

def chomsky(times=1, line_length=72):
    parts = []
    for part in (leadins, descriptions, subjects, verbs, objects, pobj, bobj, pobj,""".""", presentations):
        phraselist = list(map(str.strip, part.splitlines()))  # !3
        random.shuffle(phraselist)
        parts.append(phraselist)
    output = chain(*islice(zip(*parts), 0, times))   # !3
    return textwrap.fill(' '.join(output), line_length) + preslist + '\n\n' + disclaimer  # !3

def first_friday_finder(year, month):
	#find next first friday
    c = calendar.Calendar(firstweekday=calendar.SUNDAY)
    monthcal = c.monthdatescalendar(year, month)
    return [day for week in monthcal for day in week if day.weekday() == calendar.FRIDAY and day.month == month][0]

def generate_output(meeting_date, edition, image, location=None, location_link=None, parking_instructions=None, facebook=None, meetup=None):
  global OUTPUT, OUTPUT_CONTENT, OUTPUT_IMAGES
  text = []
  text.append("+"*3)
  text.append("title =  \"Meeting %s %s Edition\"" % ( meeting_date, edition))
  text.append("date = \"%s\"" % datetime.datetime.today().strftime('%Y-%m-%d'))
  text.append("type = \"post\"")
  text.append("author = \"antitree\"")
  text.append("image = \"/images/2600_%s.png\"" % image)
  if facebook:
      text.append("facebook = \"%s\"" % facebook)
  if meetup:
      text.append("meetup = \"%s\"" % meetup)
  text.append("+"*3)
  text.append("")
  if location:  
    if location_link:
        text.append("Location: [%s](%s)" % (location, location_link))
    else: 
        text.append("Location: %s" % location)
    if parking_instructions:
        text.append("")
        text.append("Parking directions: %s" % parking_instructions)
  text.append("")
  text.append(chomsky())
  if OUTPUT:
    try: 
        copyfile('./2600_%s.png' % image, OUTPUT_IMAGES)
    except:
        print("Image not found. make sure you generate on first.")
        print("Assuming you just copied it.")
        #sys.exit() ## TODO enable


    #write_check = input("This is about to overwrite the file at %s. That ok? (Y/n)" % OUTPUT_CONTENT) or "y"
    #if write_check.lower() == "y":
    #    f = open("%s/%s.md" % (OUTPUT_CONTENT, datetime.datetime.today().strftime('%Y-%m-%d')), 'w')
    #    f.writelines("%s\n" % t for t in text)
    #else: print("Write file skipped")

  for line in text:
        print(line)

def is_url(url):
    import re
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

today = datetime.datetime.today()
ff = first_friday_finder(today.year, today.month)
if (ff - datetime.date.today()).days < 0:
    if today.month == 12:
        nextmonth = 1
    else: 
        nextmonth = today.month + 1
    ff = first_friday_finder(today.year, nextmonth)
ff = ff.strftime('%m/%d/%Y')

meeting_date = input("What's the date of the next meeting? (%s)" % ff) or ff
location = input("What is the name of the meeting location? (%s):" % DEFAULT_LOCATION) or DEFAULT_LOCATION
location_link = input("Link to map of meeting location: (Use RIT Cyber Cyber Map)") or DEFAULT_LOCATION_LINK
if not is_url(location_link): 
    print("Proper URL not provided. What are you even doing?")
    #sys.exit()
park_bool = input("Extra parking instructions? (y/N)") or "n"
if park_bool.lower() == "y":
        parking_instructions = input("What are the instructions for parking? ")
else: 
        parking_instructions = None
        print("I guess you don't care about parking")
edition = input("What's the edition? (e.g. Trump, Black Santa): ")
image = input("What's the name alone of the image? (%s): " % edition.lower()) or edition.lower()
facebook = input("Do you have a facebook link? (%s): " % DEFAULT_FACEBOOK_GROUP) or DEFAULT_FACEBOOK_GROUP
meetup = input("Do you have a meetup link? (%s): " % DEFAULT_MEETUP_GROUP) or DEFAULT_MEETUP_GROUP
while True:
    generate_output(meeting_date, edition, image, location = location, location_link = location_link, parking_instructions = parking_instructions, meetup=meetup, facebook=facebook)
    sufficient = input("Sufficient? (Y/n) ") or "y"
    if sufficient.lower() == "y": 
        break

