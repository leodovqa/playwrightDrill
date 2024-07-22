import random


def get_nickname(name):
    print(f"Hello, {name}\n")


def game_1_to_10_guess(user_guessing):
    rnd_num = random.randrange(1, 11)
    tries = 0
    while user_guessing != rnd_num:
        tries += 1
        user_guessing = input("Wrong, try again: ")
        if int(user_guessing) == rnd_num:
            print(f"\nGreat, you guessed it. yep it was: {rnd_num}")
            return rnd_num
        elif tries > 1:
            if rnd_num > 5:
                print("\nTake a hint: it's from 6 ~ 10")
            else:
                print("\nTake a hint: it's from 1 ~ 5")
        else:
            print("\nNope you guessed the wrong number, try again")


get_nickname(input("Enter a nickname: "))
game_1_to_10_guess(input("Try to quess a number from 1 to 10: "))
