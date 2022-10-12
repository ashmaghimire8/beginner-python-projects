
import random

# def guess(x):
#     random_number = random.randint(1,x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f"Guess a number between 1 and {x}: "))
#         if guess < random_number:
#             print("Sorry the guess is low")
#         elif guess > random_number:
#             print("Sorry the guess is high")
    
#     print(f"Yay you have guessed the right answer that is {random_number} ")




def computer_guess(x):
    low = 100
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high(H), too low (L),or correct(C) ?").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay the computer guessed the number , {guess},correctly")


computer_guess(1000)