import random 
import time

#list of words to be randomized
python_functions = ['Phonology', 'Variations', 'intonation', 'Pronunciation', 'Person', 'Earth', 'Philippines', 'Information', 'Word', 'Sometimes', 'Random']

def get_random_word(word_list):
    return random.choice(word_list)

def play_game(word_list, time_limit):
    score = 0
    total_correct = 0
    total_wrong = 0
    start_time = time.time()
    
    while True:
        word = get_random_word(word_list)
        print('Type this word: ', word)
        start = time.time()

        user_input = input()

        end = time.time()

        if user_input == word and (end - start) < time_limit:
            score += 1
            total_correct += 1
            print('Correct! Your score is...', total_correct)
        else:
            score -= 1
            total_wrong -= 1
            print('Wrong answer or time expired.')
            print('Minus one, your score is...' , score)

        if end - start_time > 20:
            print('Times Up! Your final score is....' , score)
            print('Your total correct answer is....' , total_correct)
            print('Your total wrong answer is...' , total_wrong)
            break

play_game(python_functions, 5)