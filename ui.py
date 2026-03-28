def higher():
    print("Your guess is too high!")

def lower():
    print("Your guess is too low!")

def correct():
    print("You're right!")

def remaining(lives):
    if lives > 0:
        print(f"You have {lives} lives left!")
    else:
        print("You're done!")



def game_over(name, score):
    print(f"Game Over for You {name}. You got {score} points!")

def thanks(name):
    print(f'Thank you, {name}, for playing!')