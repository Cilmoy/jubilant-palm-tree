#! python3
''' randomQuizGen.py -- a python program to generate geography quizes
    on US states and their capitals in random order, along with an
    answer key '''

import random

# Quiz data -- keys are states and values are their capitals

capitals = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Pheonix',
    'Arkansas' : 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawai\'i' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe', 
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismark',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennslyvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne'
}

# Generate quiz files
amount = 2 # Change this variable to the amount of quizzes to be generated

for quizNum in range(amount):
    # Create the quiz and answer key files
    quizFile = open(f'capitalsQuiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsQuiz_answers{quizNum + 1}.txt', 'w')

    # Write out the header for the quiz
    quizFile.write('Name:\n\nDate: \n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    # Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each
    for questionNum in range(5):
        # Get right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # TODO write the questions and answers to the quiz file and answer key file
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"   {'ABCD'[i]}. { answerOptions[i]}\n")
        quizFile.write('\n')
        answerKeyFile.write(f"{questionNum + 1}.    {'ABCD'[answerOptions.index(correctAnswer)]}")
quizFile.close()
answerKeyFile.close()