import time
items = []

def print_pause(printable_value):
    time.sleep(1.5)
    print(printable_value)

def intro():
    print_pause('Hey, You have just arrived at your new job!')
    print_pause('You are in the elevator.')


def first_floor():
    print_pause('You push the button for the first floor.')
    print_pause('After a few moments, you find yourself in the Lobby.')
    
    if 'ID CARD' in items:
        print_pause('The clerk greets you, but she has already given you your ID card,so there is nothing more to do here now.')
    
    else:
        print_pause('The clerk greets you and gives you your ID card.')
        items.append('ID CARD')

    print_pause('You head back to the elevator.')
    ride_elevator()


def second_floor():
    print_pause('You push the button for the second floor.')
    print_pause('After a few moments, you find yourself in the Human Resources department.')

    if 'handbook' in items:
        print_pause("The HR folks are busy at their desks. There doesn't seem to be much to do here.")
    
    else:
        print_pause('The head of HR greets you.')
        if 'ID CARD' in items:
            print_pause('He looks at your ID card and then gives you a copy of the employee handbook.')
            items.append('handbook')
        else:
            print_pause("He has something for you, but says he can't give it to you until you go get your ID card.")
    
    print_pause('You head back to the elevator.')
    ride_elevator()


def third_floor():
    print_pause('You push the button for the third floor.')
    print_pause('After a few moments, you find yourself in the Engineering Department.')

    if 'ID CARD' in items:
        print_pause('You use your ID card to open the door.')
        print_pause('Your program manager greets you and tells you that you need to have a copy of the employee handbook in order to start work.')
        if 'handbook' in items:
            print_pause("Fortunately, you got that from HR!")
            print_pause("Congratulatons! You are ready to start your new job as vice president of engineering!")
            time.sleep(1)
        else:
            print_pause("They scowl when they see that you don't have it, and send you back to the elevator.")
            ride_elevator()

    else:
        print_pause("Unfortunately, the door is locked and you can't get in.")
        print_pause("It looks like you need some kind of key card to open the door.")
        print_pause('You head back to the elevator.')
        ride_elevator()


def ride_elevator():
    print_pause('Please enter the number for the floor you would like to visit:')
    time.sleep(1.5)
    floor = input('1. Lobby\n'
                   '2. Human resources\n'
                   '3. Engineering department\n')
    if floor == '1' :
        first_floor()

    elif floor == '2' :
        second_floor()

    elif floor == '3' :
        third_floor()

    else:
        print_pause('Please enter correct floor')
        ride_elevator()


def play_game():
    intro()
    ride_elevator()

play_game()
    
