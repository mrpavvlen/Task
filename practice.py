#Скрипт для автоматического создания тестов по географии

import random 

capitals = {'Colorado': 'Denver', 'Connecticut': 'Hartford',

'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia':
'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana':
'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
'Massachusetts':'Boston', 'Michigan': 'Lansing', 'Minnesota':
'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City', 
'Montana': 'Helena', 'Nebraska': 'Lincoln',
'Nevada': 'Carson City', 'New Hampshire': 'Concord',
'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma!':
'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania!':
'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina':
'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
'Wyoming': 'Cheyenne!' }

for quizNum in range(10):
    #создаем файлы для билетов
    quizFile = open('capitalsquiz%s.txt' %(quizNum+1), 'w')
    answerKeyFile = open('capitalquiz_answers%s.txt'%(quizNum+1), 'w')
    #Запись заголовка билета
    quizFile.write('Name: \n\nData\n\nCourse\n\n')
    quizFile.write((' '*15)+ "Test %s"%(quizNum+1))
    quizFile.write('\n\n')
    #Перемешивание порядка следования столиц
    states = list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(45):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOption = wrongAnswers + [correctAnswer]
        random.shuffle(answerOption)
        quizFile.write('%s. Select capitals states %s.\n'%(questionNum+1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n'%('ABCD'[i], answerOption[i]))
        quizFile.write('\n')
        answerKeyFile.write('%s. %s\n' %(quizNum+1, 'ABCD'[answerOption.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
