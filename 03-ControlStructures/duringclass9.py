total_nr_questions = int(input('Enter total number of questions:\n'))
correct_questions = int(input('Enter number of correctly awnsered questions:\n'))
if correct_questions >= (total_nr_questions * 0.5):
    print('Test passed')