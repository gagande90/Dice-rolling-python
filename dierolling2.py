from random import randint

counter = 1                                             # create integer variable
while True:
    random_number = randint(1, 6)    
    print('Roll:', counter, "value:", random_number)
    if random_number == 1:                              # if random number equals 1
        break                                           # break out of loop 
    counter += 1                                        # increase counter