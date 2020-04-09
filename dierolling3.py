from tabulate import tabulate
from random import randint   
 
dice_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}      # initialize dictionary to zeros
total_score = 0
 
x = int(input("Enter the number of times die to be rolled: ")) 
for roll in range(x):                         # roll 100 times inside for loop
    number_rolled = randint(1, 6)           
    dice_dict[number_rolled] += 1               # update dictionary for number rolled
    total_score += number_rolled                # increase total score

     
print('\nTotals:' + '\n' + '=' * 7)        
print(dice_dict)    
 
print('\nTotal Score:' + '\n' + '*' * 12)  
print(total_score)  


