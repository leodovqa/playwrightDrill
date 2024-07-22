import random


def get_nickname(name):
    print(f"Hello, {name}\n")
    return name


def players(user_start):
    rnd_dice1 = random.randrange(1, 7)
    rnd_dice2 = random.randrange(1, 7)
    user_start = user_start.lower()
    if user_start != 'start':
        print("You forgot to type start... heh... anyhow our AI assistant did it for you, have fun...")
        user_start = 'start'

    while user_start == 'start':
        print(f"\nFirst dice is thrown, and it got... {rnd_dice1}")
        print(f"And the second dice got... {rnd_dice2}")
        return rnd_dice1 + rnd_dice2


def dice_sum(player1_dice, player1_nick, player2_dice, player2_nick):
    print(f"\n{player1_nick} got the sun: ", player1_dice)
    print("vs: ")
    print(f"{player2_nick} got the sun: ", player2_dice)
    if player1_dice > player2_dice:
        print(f"\n{player1_nick} won. easy!")
    elif player1_dice < player2_dice:
        print(f"{player2_nick} won. easy!")
    else:
        print("OMG it's a TIE...")


player1_nick = get_nickname(input("\nEnter a nickname player 1: "))
player1_dice = players(input("\nTo throw the dices write 'start': "))
player2_nick = get_nickname(input("\nEnter a nickname player 2: "))
player2_dice = players(input("\nTo throw the dices write 'start': "))
dice_sum(player1_dice, player1_nick, player2_dice, player2_nick)
