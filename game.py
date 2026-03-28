import ui
import random
from scores import save

def check_guess(user_guess, right_guess):
    if user_guess > right_guess:
        ui.higher()
    elif user_guess < right_guess:
        ui.lower()
    else:
        ui.correct()
        return True

def check_life(lives):
    return lives > 0

def make_guess():
    lives = 15
    is_alive = True
    score = 0

    while is_alive:
        right_guess = random.randint(1,100)

        for i in range(lives):
            user_guess = int(input("Make a guess! (integer numbers between 1-100)"))
            if check_guess(user_guess, right_guess):
                score += 1
                break
            else:
                lives -= 1
                ui.remaining(lives)

        is_alive = check_life(lives)

    name = save(score)

    restart = input("Do you want to play again? (y/n)").lower()
    if restart == 'y':
        make_guess()
    elif restart == 'n':
        ui.thanks(name)