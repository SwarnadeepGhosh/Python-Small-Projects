# Creating a simple efficient program for ordering breakfast
'''
First please keep in mind :
1. Get input and use it to determine what happens next
2. Handle bad input without crashing
3. Be flexible with the input the user can enter
4. Print messages to the console, with a short pause after each one
5. Allow the player to order again if they like
6. Now we have a better idea of the specifications for the program, we can start putting it together.
'''
import time

def print_pause(printable_value):
    time.sleep(1.5)
    print(printable_value)

def intro():
    print_pause('Hello! I am Swarnadeep, the Breakfast Bot.')
    print_pause('Today we have two breakfasts available.')
    print_pause('The first is waffles with strawberries and whipped cream.')
    print_pause('The second is sweet potato pancakes with butter and syrup.')

def valid_input(prompt, options):
    while True :
        time.sleep(1)
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
            
        print_pause('Sorry, I couldn\'t understand, Please enter correct choice ...')

def get_order():
    order = valid_input("Please place your order. Would you like waffles or pancakes?\n", ['waffles','pancakes'])
    if 'waffles' in order :
        print_pause('Waffles it is!')

    elif 'pancakes' in order:
        print_pause('Pancakes it is!')
    
    print_pause('Thanks for ordering')
    print_pause('Your order will be ready shortly...')
    order_again()

def order_again():
    response = valid_input("Would you like to give another order? Please reply with 'yes' or 'no'\n",['yes','no'])
    if 'yes' in response:
        print_pause("Very good, I'm happy to take another order.")
        get_order()

    elif 'no' in response :
        print_pause('Thank You, Have a great day ! ..')
        time.sleep(1)

def order_breakfast_main() :
    intro()
    get_order()  

order_breakfast_main()
