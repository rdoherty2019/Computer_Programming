'''
Richie Doherty
'''

"""
syllabic_poetry.py
"""
# add your imports here
import listutils
import random

# this is a partial implementation of generate_word
# it contains a list of lists, with each sub list
# containing words with the same number of syllables
# ...the first sub list contains words with only one
# syllable, the second, two syllables, etc.
def generate_word(syllables):
    available_words = [
        ['age', 'roof', 'plain', 'slime', 'floor', 'fig', 'rode', 'oomph', 'flab', 'chit', 'creek', "we'll", 'brail', 'bay', 'big', 'salve', 'yaws', 'heal', 'bring', 'stir', 'bah', 'con', 'rone', 'team', 'nought', 'gill', 'rare', 'plains', 'bowls', 'wee', 'queue', 'gun', 'etch', 'set', 'mode', 'miss', 'ate', 'darn', 'rusk', 'mast', 'box', 'their', 'duds', 'depth', 'lien', 'rob', 'deek', 'word', 'quell', 'hark', 'home', 'pledge', 'brown', 'rune', 'pike', 'sprout', 'trace', 'cot', 'nob', 'nonce', 'dear', 'sense', 'sleek', 'poke', 'hut'],
        ['stunner', 'sucrose', 'begone', 'scorecard', 'humble', 'crouton', 'trimming', 'pudding', 'henchman', 'cackle', 'coffee', 'coma', 'aces', 'prudence', 'rematch', 'hipper', 'chopper', 'imprint', 'purple', 'second', 'lowbrow', 'faucet', 'bureau', 'commune', 'endive', 'stakeout', 'sourpuss', 'cave-in', 'shipyard', 'honors', 'kowtow', 'okra', 'haler', 'rattan'],
        ['echoless', 'fluidly', 'catchier', 'cathartic', 'lawnmower', 'physicist', 'huntedly', 'unzipping', 'centigrade', 'cheekily', 'tectonics', 'clearheaded', 'seditious', 'anodized', 'vehicle', 'sprightliest', 'prevention', 'vehement', 'mnemonics', 'steamroller', 'spikiest', 'persuasive', 'randomly', 'forensics', 'uneasy', 'dizziness', 'nonhuman', 'ethanol', 'connection', 'shrewishly', 'fingerprint'],
        ['nongalactic', 'lacerating', 'optometer', 'troglodytic', 'regradated', 'uniformize', 'chlorination', 'retotaling', 'acceptable', 'culmination', 'forbiddingness', 'immoveable', 'disconcerted', 'prosperity', 'vapourizing', 'profitably', 'envelopment', 'unsealable', 'librarian', 'transmissiveness', 'willowpattern', 'nationalise', 'devotedness', 'clangorously', 'likeableness', 'troubleshooting', 'weakheartedly', 'obsoleteness'],
        ['unsublimated', 'hyperanarchy', 'cylindrically', 'irrationally', 'quasipractical', 'sulfurization', 'undermeasuring', 'victoriously', 'disquietingly', 'metaphysical', 'quasihistoric', 'undesirably', 'soporiferous', 'underrespected', 'unsymmetrical', 'reliberating', 'curability', 'nonrevolution', 'nonscientific', 'marbleization', 'wearability', 'supervexation', 'misconjugating', 'inattentiveness', 'unruinable', 'incorporeal', 'stereoscopic', 'overpolicing', 'noncombustible', 'communicable', 'janitorial', 'etymologist', 'unconnectedness', 'personality', 'unmaintainable', 'geodesical', 'sociologist', 'fortitudinous', 'elimination'],
        ['disaffiliated', 'redeemability', 'misauthorization', 'renegotiated', 'zootomically', 'microbacteria', 'malleability', 'intermediaries', 'supportability', 'eliminatory', 'nonhierarchical', 'quasiadvantageous', 'palaeontology', 'typographically', 'radioactively', 'hyperpotassemic', 'collapsibility', 'selfdramatization', 'hallucinatory', 'megalomania', 'communicativeness', 'quasisatirical', 'nontechnological', 'electrosensitive', 'overintensity', 'excommunicating', 'fundamentality', 'photoelectrical', 'visualization', 'incommensurable', 'noncontinuity', 'etymological', 'overemotional'],
        ['electrometallurgist', 'discreditability', 'nonperfectibility', 'etherealization', 'inexhaustibility', 'unautomatically', 'overdeliberated', 'nonuniversality', 'encyclopaedically', 'paradoxicality', 'hieroglyphically', 'hypercivilization', 'biogenetically', 'incompatibility', 'unconstitutionalism', 'unutilitarian', 'overidealizing', 'transcendentalization']
        ]
    #the user enters an invalid number
    if syllables > 7 or syllables < 1 :
        return None
    else:
        return listutils.random_choose(available_words[syllables - 1])

def generate_line(syllables_in_line):
    #set counters
    syllables_required = syllables_in_line
    cur_syllables = 0
    line = ''

    #will run until the syllables printed ==s the syllables required
    while cur_syllables < syllables_required:
        max_syllables_word = syllables_required - cur_syllables

        #if user enters a large number this will keep it in the word index
        if max_syllables_word > 7:
            max_syllables_word = 7

        #draw a random syllabus
        syllable = random.randint(1, max_syllables_word)
        #generate a word based on the syllable
        line = line + generate_word(syllable) + ' '

        #adjusting counter
        cur_syllables += syllable
        #reseting max
        max_syllables_word = 0
    return line

def generate_lines(all_lines):
    #setting accumulator
    lst = []
    for i in range(len(all_lines)):
        #add on the line
        lst.append(generate_line(all_lines[i]))
    return lst

#user entry
user = input("""I would like to write some poetry for you. Would you like a...
  * (h)aiku
  * (t)anka
  * (r)andom 5 line poem, or do you want to
  * (s)pecify lines and syllables for each line? \n>""")

if user == 'h' or user == 'H':
    print("Here is your poem (5-7-5):")
    print("=====")
    poem = generate_lines([5, 7, 5])
    #printing out the lines of poem
    for i in range(len(poem)):
        print(poem[i])

elif user == 't' or user == "T":
    print("Here is your poem (5-7-5-7-7):")
    print("=====")
    poem = generate_lines([5, 7, 5,7,7])
    for i in range(len(poem)):
        print(poem[i])

elif user == 'r' or user == 'R':
    syll = listutils.random_fill(1, 10, 5)
    print(listutils.join_elements_with('-', syll))
    print("=====")
    poem = generate_lines(syll)
    for i in range(len(poem)):
        print(poem[i])

#user entered syllable
elif user == 's' or user == 'S':
    #accumulators and condtionals
    test = False
    line = 1
    sylls = []

    while test == False:
        #user entry
        syll = int(input("How many syllables for lines " + str(line)+'?\n>'))
        #add it onto list
        sylls.append(syll)
        #reseting condition
        ans = input("There are currently " + str(line)+". Add another line (y/n)? \n>")
        #updating counter
        line += 1
        if ans.lower() == 'n':
            test = True
    #print out poem after user ends syllable entry
    print(listutils.join_elements_with('-', sylls))
    print("=====")
    poem = generate_lines(sylls)
    for i in range(len(poem)):
        print(poem[i])

#user entry error
else:
    print('ERROR')
    print("""A crash reduces
Your expensive computer
To a simple stone.""")