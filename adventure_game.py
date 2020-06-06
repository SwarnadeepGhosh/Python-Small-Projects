# https://github.com/SwarnadeepGhosh

import time
import random


def print_pause(printable_text):
    time.sleep(1.5)
    print(printable_text+"\n")


def intro():
    print_pause('You find yourself standing in an open field, filled with '
                'grass and yellow wildflowers.')
    print_pause('Rumor has it that a gorgon is somewhere around here, and '
                'has been terrifying the nearby village.')
    print_pause('In front of you is a house.')
    print_pause('To your right is a dark cave.')
    print_pause('In your hand you hold your trusty (but not very effective)'
                ' dagger.') 


def fight_or_run(items, demon):
    print_pause("Would you like to (1) fight or (2) run away ?")
    time.sleep(1.5)
    fight_choice = input('What would you like to do? (Enter 1 or 2.)\n')
    if fight_choice == '1':
        if 'sword' in items:
            print_pause("\nAs the "+demon+" moves to attack, you unsheath your"
                        " new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your hand "
                        "as you brace yourself for the attack.\n")
            print_pause("But the "+demon+" takes one look at your shiny new "
                        "toy and runs away!")
            print_pause("You have rid the town of the "+demon+". You are "
                        "victorious!\n\n")

        else:
            print_pause("\nYou do your best...")
            print_pause("but your dagger is no match for the "+demon+".\n")
            print_pause("You have been defeated!\n\n")

        play_again()

    elif fight_choice == '2':
        print_pause("You run back into the field. Luckily, you don't seem "
                    "to have been followed.")
        field(items, demon)

    else:
        print_pause("Please enter correct choice ...")
        fight_or_run(items, demon)


def house(items, demon):
    print_pause("\nYou approach the door of the house.")
    print_pause("You are about to knock when the door opens and out "
                "steps a "+demon+".\n")
    print_pause("Eep! This is the "+demon+"'s house!")
    print_pause("The "+demon+" attacks you!")
    print_pause("You feel a bit under-prepared for this, what with "
                "only having a tiny dagger.\n")
    fight_or_run(items, demon)


def cave(items, demon):
    if 'sword' in items:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good "
                    "stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")

    else:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        items.append('sword')
        print_pause("You discard your silly old dagger and take the "
                    "sword with you.")
        print_pause("You walk back out to the field.\n")

    field(items, demon)


def play_again():
    time.sleep(1.5)
    play_again = input("Would you like to play again? (y/n)\n").lower()
    if play_again == 'y':
        print_pause('Excellent! Restarting the game ...\n')
        play_game()

    elif play_again == 'n':
        print_pause("Exiting game . . .\n")
        print_pause("Thanks for playing. See you next time ! ...\n\n")
        time.sleep(1)

    else:
        print_pause("Please enter 'y' or 'n'")
        play_again()


def field(items, demon):
    print_pause('Enter 1 to knock on the door of the house.')
    print_pause('Enter 2 to peer into the cave')
    time.sleep(1.5)
    place_choice = input('What would you like to do? (Enter 1 or 2.)\n')

    if place_choice == '1':
        house(items, demon)

    elif place_choice == '2':
        cave(items, demon)

    else:
        print_pause("Please enter correct place_choice (1 or 2) ...")
        field(items, demon)


def play_game():
    items = []
    demon = random.choice(['flaire', 'bakasura', 'dragon', 'alastor',
                           'baron', 'pirate', 'gorgon'])
    intro()
    field(items, demon)


play_game()
