import random
from typing import List, Tuple

from src.utils import (print_error, print_novalid, print_success, print_warning)


class Wordle:
    def __init__(self, filepath, word_len=5):
        self.word_len = word_len
        data = self.read_file(filepath)
        self.words = [item[0] for item in data]

    def read_file(self, filepath: str) -> List[Tuple]:
    # read data
        with open(filepath) as f:
            data = f.read()

            # split, make list of tuple, and remove None
            data = [tuple(item.split(',')) for item in data.split('\n')[1:] if bool(item) == True]

            # change data type to int for frequency
            data = [(tup[0], int(tup[1])) for tup in data]

            #sort frequency as decending
            data = sorted(data, key=lambda x: x[1], reverse=True)

            # select 5 letters words
            data = list(filter(lambda w: len(w[0])==self.word_len, data))

        return data


    def words_check(self, word, guess_word):
        # check valid letter, invalid position, invalid letter, invalid word
            for w, g_w in zip(word, guess_word):

                # valid letter
                if w == g_w:
                    print_success(f' {g_w} ')

                # invalid position
                elif g_w in word:
                    print_warning(f' {g_w} ')

                #invalid word
                elif g_w not in word:
                    print_error(f' {g_w} ' )

                # word does not exist
                else:
                    print_novalid(f' {g_w} ')


    def run(self):

        # select the random word
        word = random.choice(self.words)

        num_try = 5

        while True:
            guess_word = input(f'Please enter the 5 letters word and enter q for exit: ')
            if guess_word == 'q':
                break

            num_try -= 1
            if num_try==0:
                print_error(f'Game is over! You are a NOOB:). Correct answer is: {word}')
                break


            if len(guess_word) != 5:
                print(f'the word is not 5 letters. Correct it!')
                continue

            self.words_check(word, guess_word)

            # Check
            if word == guess_word:
                print_success('Congratulations!')
                break





