# locker-rental
For this personal project, I wanted to work with python dictionaries. To implement this logic, I chose to make a locker rental system. 

Let's break this project down a bit. Here are the anticipated project requirements:
1. Specify if a locker is available to rent to a customer at time of service
2. Keep track of lockers that are in use and those that are available to rent
3. When renting a locker -- give the user a randomly generated number combination to access their locker
4. The user will need this code to open their locker and place up to 3 items inside (this part is just for fun!): jacket, bag, car keys
5. When the user is done with the locker -- the locker will go back to available and the combination code with be set to None until it is rented again and then a new combination will be generated (may extend this to not be equal to the last combination given or for all combinations given for the day)
6. Could add access for management in the case a locker is locked/inaccessible for an unknown reason or if it needs to be unlocked and a key is not available -- would have to implement this in a secure manner
7. Could keep track of time and rent lockers for a period of time (15 minutes, 30 minutes, 1hr, 2hr, etc.,) -- if the timer runs out -- items are put in lost and found and locker becomes available to rent again and key is reset to None
8. If #7 is implemented -- empty out lost and found every shift (if it is rented for an event -- at the end of the shift for the day it would be emptied for example)

Work for this has been paused until further notice -- Stay tuned for more updates!
