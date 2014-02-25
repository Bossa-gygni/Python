
# this is a Quiz script in Alpha stages, designed to be inserted into a bot for use on a irc.
# intro
from random import randint

solved = 0
total_num_q = 0


print'\n'
print '\t\t\t\033[1;31mWelcome Quiz Contestants, get ready for action packed Quiz questions\033[1;m' # red
print '\t\t\t\033[1;31mIf you get the question correct then weldone, but if you don\'t YOU ARE GOING TO GET ABUSED\033[1;m'
print '\t\t\t\033[1;31mWith various insults, so get ready for lots of lulz and ofc rage quitting lol\033[1;m'
print '\t\t\t\033[1;31mFor questions and ideas to better the Quiz master. please contact Paradox\033[1;m'
print'\n'
print '\t\t\t\t\t\t\t\t\033[1;33mNow get ready because the quiz is about to start!!\033[1;m' # yellow
print'\n'
print '\033[1;32m-\033[1;m' * 100 # colour (green grass)
#
#-----------------------------------------Easy Questions-----------------------------------------
#-----------------------------------------Question 1---------------------------------------------
print "On what day of the year is St Georges day held?:" ,
print "23rd April(1), 15th March(2), 25th December(3):"
Q1 =int( raw_input())

if Q1 <= 1 :
    print( 'you are correct, welldone! ' )
    solved = solved + 1
elif  Q1 <= 2 :
    print( 'wrong answer you total faggot, learn to google' )
else :
    print( 'GO back to school Billy Madison' )
print '\033[1;32m-\033[1;m' * 100
#--------------------------------------------Question 2------------------------------------------------
print('What colour is the bullseye on a standard dartboard?:')
print "Blue(1) , Pink(2) , Red(3):"
Q2 =int( raw_input())

if Q2 <= 1 :
    print( ' You are a complete retard, the special bus is on its way to collect you!! ' )
elif Q2 <= 2 :
    print( 'do you have downs or something, you should have paid more attention at school!!! ' )
else :
    print( 'Correct answer, grab your self a beer! ' )
    solved = solved + 1
print '\033[1;32m-\033[1;m' * 100
#----------------------------------------Question 3--------------------------------------------------
print('What was Mohammad Ali\'s bith name?:')
print "Paul Peacock(1) , Cassius Clay(2) , Clarke Kent(3):"
Q3 =int(raw_input())

if Q3 <= 1 :
    print( ' Your Birth Certificate is an apology from the condom factory! ' )
elif Q3 <= 2 :
    print( 'You are correct, you are not a faggot! ' )
    solved = solved + 1
else :
    print( 'If you were twice as smart, you\'d still be stupid! ' )
print '\033[1;32m-\033[1;m' * 100
#-----------------------------------------question 4---------------------------------------------------
print( 'According to the old proverb all roads lead to which capital city?:')
print "London(1) , New York(2) , Rome(3):"
Q4 =int(raw_input())

if Q4 <= 1 :
    print( 'Out of 100,000 sperm, you were the fastest! ' )
elif Q4 <= 2 :
    print( 'are you serious?? ' )
else :
    print( 'you are correct! carry on you faggot!! ' )
    solved = solved + 1

#----------------------------------Normal level questions---------------------------------------------------------------
print '\033[1;32m-\033[1;m' * 100 # to make a splitter line
print '\033[1;32m-\033[1;m' * 100 # double splitter line
print '\033[1;33mWeldone you have made it though the Easy Round, prepare for the next level of quiz fellow faggot\'s, good luck\033[1;m'
print '\033[1;32m-\033[1;m' * 100
print '\033[1;32m-\033[1;m' * 100
#-------------------------------------question 1-----------------------------------------------------
print( ' What was left in Pandora\'s box after all the evil had escaped?:')
print "Hope(1) , Dispair(2) , Dope(3): "
Q5 =int(raw_input())

if Q5 <= 1 :
    print( 'You are correct smarty pants! ' )
    solved = solved + 1
elif Q5 <= 2 :
    print( 'Im in Dispair you chose to take this quiz!! ' )
else:
    print( 'GTFO now faggot! ' )
print '\033[1;32m-\033[1;m' * 100
#--------------------------------------Question 2----------------------------------------------------------------------
print( ' If you travel due east from NYC, which country would you hit first?:')
print "North Korea(1) , Japan(2) , Portugal(3):"
Q6 =int(raw_input())

if Q6 <= 1 :
    print( 'If you really want to know about mistakes you should ask your parents! ' )
elif Q6 <= 2 :
    print('The only positive thing about you is your HIV status! ' )
else:
    print( 'Weldone you are correct, im crying with joy! ' )
    solved = solved + 1
print '\033[1;32m-\033[1;m' * 100
#-------------------------------------Question 3-----------------------------------------------------------------------
print "*Surpise Riddle*" * 4
print "-" * 100
print( 'What has a mouth but can\'t chew?:')
print "Dolly Parton(1) , Ozzy Osbourne(2) , A river(3):"
Q7 =int(raw_input())

if Q7 <= 1 :
    print( 'Here\'s 20 cents, call all your friends and give me back the change, faggot! ' )
elif Q7 <= 2 :
    print( 'you\'re so stupid you got fired from the m&m factory for throwing out all the w\'s')
else:
    print( 'Weldone, you are correct, Human kind has some sort of chance! ' )
    solved = solved + 1
print '\033[1;32m-\033[1;m' * 100
#-----------------------------------------Question 4-------------------------------------------------------
print( 'Which planet is the eighth planet from the sun with a mass 17 times of that of earth?:')
print "Neptune(1) , The sun(2) , Your mums left tit(3):"
Q8 =int(raw_input())

if Q8 <= 1 :
    print( 'You are correct, and i\'d like to add im sorry you didn\'t have any friends in school')
    solved = solved + 1
elif Q8 <= 2 :
    print( 'you must be the reason why some parents eat their young' )
else:
    print( 'some day you will know your 1Q and wish you hadn\'t learned it' )

#-----------------------------------------------------------------------------------------------------------------------
print '\033[1;32m-\033[1;m' * 100
print '\033[1;32m-\033[1;m' * 100
print '\033[1;33mWeldone you have made it though the Normal round, prepare for the next level of quiz, good luck\033[1;m'
print '\033[1;32m-\033[1;m' * 100
print '\033[1;32m-\033[1;m' * 100
#------------------------------------------Surpise Riddle---------------------------------------------------------------
print "*Surpise Riddle*" * 4
print '\033[1;32m-\033[1;m' * 100
print 'What gets whiter the diriter it gets?:'
print "Your mon(1) , Chalkboard(2) , Micheal Jackson(3):"
Riddle =int(raw_input())

if Riddle <= 1 :
    print( 'I have no comment, but maybe you should kill your self')
elif Riddle <= 2 :
    print( 'you are correct, weldone!! you are not going to get abused by the d tonight' )
    solved = solved + 1
else:
    print( 'you have major childhood trama!!' )
print '\033[1;32m-\033[1;m' * 100
#--------------------------------Question 1 (hard quiz)-----------------------------------------------------------------
print( 'which NBA basketball \'bad boy\' was renowned for dying his hair bright colours?:')
print 'Ronald McDonald(1) , Dennis Rodman(2) , Isiah Thomas(3):'
Q9 =int(raw_input())

if Q9 <= 1 :
    print( 'Scuse  me,  I can\'t seem to find my dick.  Mind if I look in your mother\'s mouth?' )
elif Q9 <= 2 :
    print( 'You are correct, even i had to google that one! lol')
    solved = solved + 1
else:
    print('Is that an accent, or is your mouth just full of sperm?')
print '\033[1;32m-\033[1;m' * 100
#-------------------------------------Question 2------------------------------------------------------------------------
print('The ELO system is used to rank players in which game?:')
print('Chess(1) , Rugby(2) , Ping Pong(3):')
Q10 =int(raw_input())

if Q10 <= 1 :
    print('Weldone..you must have googled that faggot!')
    solved = solved + 1
elif Q10 <= 2 :
    print( 'are you retarded bro!')
else :
    print('you are the love child of a homeless man and a whore!!')
#--------------------------------------PUzzel------------------------------------------------------------------
print '\033[1;32m-\033[1;m' * 100
print '\033[1;32m-\033[1;m' * 100
print "*Surpise pudzel*" * 5
print '\033[1;32m-\033[1;m' * 100
#
def play(num1, num2, type, solved):
    """ The main play function"""
    def sp_type():
        type = raw_input("Specify the question type(multiplication:M, addition:A, subtraction:S, division:D):")
        if type not in ['M','A','S','D']:
            print "Please input only char M,S,A and D"
        return type
    type = ""
    while type not in ['M','A','S' ,'D']:
        type = sp_type()
    if type == "M":
        ans = input("What's %d times %d? " % (num1, num2))
        result = num1 * num2
    if type == "A":
        ans = input("What's %d plus %d? " % (num1, num2))
        result = num1 + num2
    if type == "S":
        ans = input("What's %d minus %d? " % (num1, num2))
        result = num1 - num2
    if type == "D":
        ans = input("What's %d divided by %d? " % (num1, num2))
        result = num1/num2

    if ans == result:
        print "That's right -- well done.\n"
        solved = solved + 1
    else:
        print "No, I'm afraid the answer is %d.\n" % result
    return solved
def start_puzzle(solved, total_num_q):
    leval = ''
    play_leval = ['intermediate', 'hard']
    while leval not in play_leval:
        leval = raw_input("Which leval you wanted to be in(intermediate, hard): ")
        if leval not in play_leval:
            print "Please enter correct leval name.."
    num_q = input("Please give us the number of question you want to attempt: ")
    try:
        if int(num_q):
            pass
    except:
        print "Please enter only integet value"
    total_num_q = total_num_q + num_q
    for number_q in range(num_q):
        if leval == 'intermediate':
            num1 = randint(1, 20)
            num2 = randint(1, 20)
            solved = play (num1, num2, type, solved)
        elif leval == 'hard':
            num1 = randint(1, 30349666)
            num2 = randint(1, 303496166)
            solved = play (num1, num2, type, solved)
    return (solved, total_num_q)
print '\033[1;32m-\033[1;m' * 100
inp = "yes"
def loopingFunction(play):
    while play == 1:
        i = play + 1
        print i
while inp != 'no':
    solved,total_num_q = start_puzzle(solved,total_num_q)
    inp = raw_input("want to start puzzle(yes/no):")
print '\033[1;32m-\033[1;m' * 100

#-------------------------------end part----------------------------------------------------------------

print '\nYou got %d of them right' % (solved)
print "you're done it faggot, you completed the Quiz, take it again faggot ;) :) !"



