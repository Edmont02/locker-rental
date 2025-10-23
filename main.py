import random

# nested dictionaries for each locker within the set of lockers
locker1 = {
    # tells if locker is available (True) or not (False)
    "Available" : False,
    # key is initialized to None -- key will be set when rented
    "Key": None,
    # items currently in locker
    "Items" : ["book", "laptop", "pen"]
}
locker2 = {
    "Available" : True,
    "Key": None,
    "Items" : []
}
locker3 = {
    "Available" : True,
    "Key": None,
    "Items" : []
}

locker4 = {
    "Available" : False,
    "Key": None,
    "Items" : ["purse", "keys", "sunglasses"]
}

# provides access to every locker
lockers = {
    "1": locker1,
    "2": locker2,
    "3": locker3,
    "4": locker4
}

# function to generate a random 6-digit key
def generate_key():
    return ''.join(random.choices('0123456789', k=6))

# function for renting a locker
def rent_locker():
    # search for available lockers
    available_lockers = [locker_number for locker_number, locker in lockers.items() if locker["Available"]]
    print(f"These are the available lockers: {available_lockers}")
    # ask which locker to rent
    print(f"Which locker would you like to rent?")
    locker_number = input()
    # check if locker is available to rent
    if lockers[locker_number]["Available"] == True and locker_number in available_lockers:
        # create a key for renting locker
        key = generate_key()
        # assign key to the renting locker
        lockers[locker_number]["Key"] = key
        # mark locker as no longer available
        lockers[locker_number]["Available"] = False
        # return the key and locker number
        return f"Locker {locker_number} rented successfully. Your key is {key}."
    # if locker in lockers.items() is not available
    elif lockers[locker_number]["Available"] == False and locker_number in available_lockers:
        return f"Locker {locker_number} is not available. Please choose another locker."
        
# function for customer to access locker being rented
def access_locker():
    # get the locker number from the customer
    print("Enter your locker number: (eg.: 1, 2, ..., n): ")
    locker_number = input()
    # ask for the key/pin code for the locker to access it
    print(f"You entered \"Locker {locker_number}\". Please enter the pin code for your locker: ")
    customer_key = input()
    # check that the key the customer gave is correct
    if customer_key != lockers[locker_number]["Key"]:
        return "The pin you entered is incorrect. Try again."
    elif customer_key == lockers[locker_number]["Key"]:
        return "You can access your locker!"
    else:
        return "There was an error with access_locker."
        
# function for putting item(s) in locker
def place_items():
    while(1):
        # ask if user would like to place an item in their locker
        print("Would you like put an item in your locker? (Y/y or N/n)")
        answer = input()
        # if yes, ask for item and add it to locker
        if answer.lower() == 'y':
            print("What item would you like to place in your locker?")
            item = input()
            lockers["2"]["Items"].append(item)
            # print item(s) in locker
            print(f"In locker 2 items: {lockers["2"]["Items"]}")
        # if no -- break from while loop
        elif answer.lower() == 'n':
            break
        # there was an issue with user input
        else:
            print("User Input Error. Please type 'y' for yes or 'n' for no.")
            
# remove item(s) from locker
def remove_items():
    while(1):
        #ask if user would like to remove an item from their locker
        print("Would you like to remove an item from your locker? (y or n)")
        answer = input()
        # if yes, ask for item name
        if answer.lower() == 'y':
            print(f"These are the items in your locker: {lockers["2"]["Items"]}")
            print("What item would you like to remove from your locker?")
            item = input()
            # scan locker for matching item
            # if match -- remove item
            if item in lockers["2"]["Items"]:
                lockers["2"]["Items"].remove(item)
            # if item not found -- change nothing
            else:
                print("Item not found in locker.")
            print(f"Your items are now: {lockers["2"]["Items"]}")
        # if no, exit loop
        elif answer.lower() == 'n':
            break
        # else - incorrect input, try again
        else:
            print("User Input Error. Please type 'y' for yes or 'n' for no.")
    
# function for returning locker and retrieving items
def locker_return():
    while(1):
        print("Are you ready to return your locker? (y or n)")
        answer = input()
        if (answer.lower() == 'y'):
            # logic for returning locker and retrieving items
            print(lockers['2'])
            print("Type r to retrieve your items and return your locker.")
            answer = input()
            if (answer.lower() == 'r'):
                lockers['2']['Items'] = []
                print("Items retrieved successfully.")
                lockers['2']['Available'] = True
                lockers['2']['Key'] = None
                print("Locker returned successfully.")
                print(lockers['2'])
                break
            else:
                print("Item retrieval cancelled.")
                break
        elif (answer.lower() == 'n'):
            print("Locker return cancelled.")
            break
        else:
            ("User Input Error. Please type 'y' for yes or 'n' for no.")

# main function for user interaction
if __name__ == '__main__':
    # # test renting a locker
    # print(rent_locker())
    
    # # testing accessing a locker
    # print(access_locker())
    
    # # testing place_items
    # place_items()
    
    # # testing remove_items
    # # remove_items()
    
    # # testing locker_return
    # locker_return()
    
    print("Welcome to the Locker Rental System!")
    # main loop for user interaction
    while (1):
        # display menu options
        print("Please enter one of the following options:")
        print("1. Rent a locker")
        print("2. Access your locker")
        print("3. Place items in your locker")
        print("4. Remove items from your locker")
        print("5. Return your locker")
        print("6. Exit")
        option = input()
        
        # option switch for menu selection
        switch = {
            "1": rent_locker,
            "2": access_locker,
            "3": place_items,
            "4": remove_items,
            "5": locker_return,
            "6": exit
        }
        
        # handle menu selection
        if option in switch:
            if option == "1":
                print(rent_locker())
            elif option == "2":
                print("Under development.")
            elif option == "3":
                print("Under development.")
            elif option == "4":
                print("Under development.")
            elif option == "5":
                print("Under development.")
            elif option == "6":
                print("Thank you for using the Locker Rental System. Goodbye!")
                break
        # invalid option handling
        else:
            print("Invalid option. Please select a number from 1 to 6.")