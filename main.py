# stone paper and scissors game 
'''
stone and paper - paper winner 
paper and scissors - scissors winner
stone or scissors - stone winner 
'''
# the user have to make 10 points to win .


import random 

options = ["stone","paper","scissors"]
user_score = 0
computer_score = 0
chances = 0 

# comp_choice = random.choice(options)
# print (comp_choice)   #for checking the program


print (" STONE , PAPER , SCISSORS GAME ")
print("")
print("")

print ("you have 10 chances . you and the computer will play this game ")
print ("the one who will gain more points will be the winner of the game ")
print("starting the game ")

print("")
print("")

# print("The computer has chose. now is your turn.")
print("press 1 to choose stone")
print("press 2 to choose paper")
print("press 3 to choose scissors ")
try:
    for i in range (1,11):
        print ("the computer has chose . now is your turn")
        user_choice = int(input())
        comp_choice = random.choice(options)

        if user_choice == 1:
            print ("you have chosen stone")
            chances = chances+1
            print ("you have ",10- chances,"chances left")
            

        elif user_choice == 2:
            print('you have chosen paper ') 
            chances = chances +1 
            print ("you have ",10 -chances,"chances left")
            


        elif user_choice  == 3:
            print ("you have chosen scissors ")
            chances = chances + 1
            print ("you have ",10 -chances,"chances left") 
            


        else :
            print ('invalid input try again.') 
            chances = chances+1
            print ("you have ",10 -chances,"chances left")



        if user_choice == 1 and comp_choice == 'stone':
            print ("the computer choose",comp_choice)
            print ('this is a tie')
            print("the score of the computer is ",computer_score)
            print ("your score is",user_score)


        elif user_choice == 2 and comp_choice == 'paper':
            print ("the computer choose",comp_choice)
            print ('this is a tie')
            print("the score of the computer is ",computer_score)
            print ("your score is",user_score)


        elif user_choice == 3 and comp_choice == 'scissors':
            print ("the computer choose",comp_choice)
            print ('this is a tie')
            print("the score of the computer is ",computer_score)
            print ("your score is",user_score)


        elif user_choice == 1 and comp_choice == 'paper':
            print ("the computer choose",comp_choice)
            print ('the computer is the winner ')
            computer_score = computer_score+1
            print("the score of the computer is ",computer_score)
            print ("your score is",user_score)


        elif user_choice == 2 and comp_choice == 'stone':
            print ("the computer choose",comp_choice)
            print ('you are the winner')
            user_score = user_score + 1
            print("the score of the computer is ",computer_score)
            print ("your score is",user_score)


        elif user_choice == 2 and comp_choice == 'scissors':
            print ("the computer choose",comp_choice)
            print ('the computer is the winner ')
            computer_score =computer_score+1
            print("the score of the computer is ",computer_score)
            print ("your score is",user_score)


        elif user_choice == 3 and comp_choice == 'paper':
            print ("the computer choose",comp_choice)
            print ('you are the winner ')
            user_score =user_score+1
            print("the score of the computer is ",computer_score)
            print ("your score is",user_score)


        elif user_choice == 1 and comp_choice == 'scissors':
            print ("the computer choose",comp_choice)
            print ('you are the winner  ')
            user_score + user_score +1
            print("the score of the computer is ",computer_score)
            print ("your score is",user_score)


        elif user_choice == 3 and comp_choice == 'stone':
            print ("the computer choose",comp_choice)
            print ('the computer is the winner ')
            computer_score= computer_score+1
            print("the score of the computer is ",computer_score)
            print ("your score is",user_score)
except Exception as e :
    print (e)
    print("")
    print('')
    print ("do you want to play ??")
    print ("if yes , then start from first")

print ("the score of the computer is :",computer_score )
print ("your score is :",user_score)

if computer_score > user_score:
    print ("the computer is the winner ")
elif user_score>computer_score:
    print ("you are the winner ")
else :
    print ("its a tie ")


print ("Do you want to play again?")
try:
    continueans = int(input("press 1 to choose yes and press 2 choose no"))

    if  continueans == 1:
        print ("please start again from first by clicking the run button")
        pass
    elif continueans==2:
        print ("ok, thank you for using our game ")
    else:
        print ("wrong input . thank you for using our game")
except Exception as e:
    print (e)
