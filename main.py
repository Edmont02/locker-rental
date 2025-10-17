import random
import string

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
    "Items" : ["wallet, phone"]
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

# rent locker function
def rent_locker():
    # check that locker is available
    # if not available, continue searching for an available locker
    for locker_number, locker in lockers.items():
        # if available, rent locker
        if locker["Available"]:
            # create a key for renting locker
            key = generate_key()
            # assign key to the renting locker
            lockers[locker_number]["Key"] = key
            # mark locker as no longer available
            locker["Available"] = False
            # return the key and locker number
            return f"Locker {locker_number} rented successfully. Your key is {key}."
        # if locker in lockers.items() is not available -- continue searching
        else:
            continue
        # next -- make a conditional statement for if all lockers are taken / not available    
        
# function to for customer to access locker being rented
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
        return "There was an error with place_items."
        
# function for putting items in locker
def place_items():
    # if key_given is equal to key for specific locker -- continue with item logic
    # if key_given is not the same as key for specific locker -- give three chances and then lock continued attempts
    pass
    
# function for returning locker and retrieving items
def locker_return():
    # if key_given is equal to key for specific locker -- continue with returning locker and item retrieval logic
    # if key_given is not the same as key for specific locker -- give three chances and then lock continued attempts
    pass

# main function for user interaction
if __name__ == '__main__':
    # test renting a locker
    print(rent_locker())
    # testing accessing a locker
    print(access_locker())