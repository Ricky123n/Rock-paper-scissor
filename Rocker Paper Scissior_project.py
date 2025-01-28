import random


user_choice=int(input("enter your choice :type 0 for rock, 1 for paper, 2 for scissors: "))
computer_choice=random.randint(0,2)
print("computer choose: ")
print(computer_choice)
if(computer_choice == user_choice):
    print("Its a draw.")
elif(computer_choice == 0 and user_choice==2):
    print("You lose")
elif(computer_choice ==2 and user_choice ==0):
    print("You win")    
elif(computer_choice > user_choice):
    print("you lose")
elif(computer_choice < user_choice):
    print("You win")
     
            
