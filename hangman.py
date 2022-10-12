import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word=random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word =  get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 7

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        print("you have",lives,"lives left and you have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('current word: ',' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            
            else:
                lives = lives - 1
                print("your letter,",user_letter,'is not in the word')
        
        elif user_letter in used_letters:
            print("\nyou have already used that letter. guess another letter")
        else:
            print("\n That is not a valid letter")

    if lives == 0:
        print(lives_visual_dict[lives])
        print("you died, sorry. The word was",word)
    else:
        print("YAY!you guessed the word",word," correctly")

if __name__ == '__main__':
    hangman()
