#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Langsing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raeigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsyvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.
for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile = open('Capitalsquiz%s.txt' % (quizNum + 1), 'w')                       
    answerKeyFile = open('Capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    '''Since 35 quizzes will have to be created, '35' is passed to range(), with quizNum representing
    the number of each of the quizzes. quizFile and answerKeyFile represent the two different types of
    files that will be created. The name of the files themselves are 'Capitalsquiz%s.txt' and
    'Capitalquiz_answers%s.txt'. The '%' is quizNum, and '%s' is the string version of quizNum. So as to
    write content to the files, 'w' is passed to open them in write mode. For each iteration, quizNum
    will be amped up by 1'''

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')                                 
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))    
    quizFile.write('\n\n')

    '''These strings written to quizFile (Capitalsquiz%s.txt) will be the heading for the quizzes,
    which include the name, date, period, title, as well as the form number (quizNum)'''

    # Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    """All of the keys in the "capitals" dictionary, which are the states, are passed to the list,
    'states', which is then 'shuffled' by random.shuffle(). This function is used to randomize
    the order of a list"""
    

    # Loop through all 50 sates, making a question for each.
    for questionNum in range(50):
    '''This for loop will generate the content for the quizzes, which contain 50 questions each'''

        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        
        ''' The correct answer is aquired by passing states[questionNum] to capitals. Each number in
        the for loop (questionNum) is passed as an index to the "states" list.  This index, containing
        the name of the state, is then passed to the "capitals" dictionary as an argument, in which it 
        is assigned the corresponding capital of that state. This value is then stored into the correctAnswer
        variable.

        The wrong answers are stored inside the list "wrongAnswers", which contains all of the
        values (capitals) in the "capitals" dictionary. Since it also contains the correct answer, it is
        removed from the list by calling "del" to the index of the correct answer. "wrongAnswers" is then
        set to 3 randomly selected values in the list using random.sample(), which returns a specific number
        of random values from a list. The 4 total answers are then stored in the list "answerOptions",
        which is then shuffled as an anti-copying measure for the students.'''
        
        # Write the question and the answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,
            states[questionNum]))
        for i in range(4):
            quizFile.write('   %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        '''The string passed to quizFile will be repeated 50 times. The first appearance of %s is the
        iteration number of "questionNum", and the second one is the state with the iteration of quizNum
        as it's index.'''

        '''The for loop creates multiple strings containing the possible answers. The first appearance of
        %s will be the letters A,B,C, and D, and the second appearance is the answers themselves. Both the
        letters and the state answers were returned by calling the index given to them by i'''
        
        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()

    ''' This will write the answers to answerKeyFile (capitalquiz_answers%s.txt). The first appearance of
    %s is the iteration number of questionNum, and the second is the letter answer. The letter answer is
    obtained by passing answerOptions.index(correctAnswer) to 'ABCD', which will search the 'answerOptions'
    list for the index of 'correctAnswer'. The answer is then matched to the letter with the same iteration
    number assigned by 'i' in the inner for-loop.








































    

    


