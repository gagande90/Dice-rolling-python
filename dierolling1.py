from random import randint                         

repeat = True                                      
while repeat:                                 #while loop for getting game to run infinite times      
    print("You rolled", randint(1, 6))             
    print("Do you want to roll again?")
    rsp = input().lower().strip()                  
    repeat = ("y" == rsp) or ("yes" == rsp)   #asking user for input     

print("*** End of Game ***")                       

