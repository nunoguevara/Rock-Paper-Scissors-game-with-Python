import random as rm
import time as tm
import os

rpscom = {'1' : 'Rock', '2' : 'Paper', '3' : 'Scissors'}

x = 0
y = 0
a = 0
b = 0
r = 0
c = 0

num = ["1", "2", "3"]
bignum = [957, 927, 578, 847, 574, 577, 988]

class game:
    def game():
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

class menu:
    def menu():
        print("Rock, Paper, Scissors Game")
        print("1. Play the Game")
        print("2. Exit the game")
        print("3. About this game")
        print("4. My statistics on this game")
        
while True:
    
    menu.menu()
    choice = str(input("Please input your choice: "))
    if choice == "1":
        while True:
            bignumrm = rm.choice(bignum)
            r += 1
            game.game()
            rps = str(input("Please input your choice: "))
            if rps in rpscom:
                print("Wait for computer turns...")
                rpscomran = rm.choice(num)
                tm.sleep(0.5)
                print("Your output is: ", rpscom[rps])
                print("Computer output is: ", rpscom[rpscomran])
                if rps == "3" and rpscomran == "2":
                    print("You win")
                    x += 1
                elif rps == rpscomran:
                    print("Draw")
                elif rps == "2" and rpscomran == "1":
                    print("You win")
                    x += 1
                elif rps == "1" and rpscomran == "3":
                    print("You win")
                    x += 1
                else:
                    print("You lose")
                    y += 1
                    
                print("Counting your score....")
                tm.sleep(0.3)
                print("Your score: ", x)
                print("Your opponent's score: ", y)
                if x > 4:
                    print("You are the winner with score of ", x, ":", y)
                    print("Balance +", bignumrm)
                    tm.sleep(2)
                    a += 1
                    x = 0
                    y = 0
                    c += bignumrm
                    os.system('cls' if os.name == "nt" else 'clear')
                    break
                elif y > 4:
                    print("You lose with the score of ", x, ":", y)
                    tm.sleep(2)
                    y = 0
                    x = 0
                    b += 1
                    os.system('cls' if os.name == "nt" else 'clear')
                    break
            else:
               print("Invalid choice, back to the menu...")
               print("Your round progress won't be reset...")
               tm.sleep(3)
               break
    elif choice == "2":
        print("Leaving game....")
        tm.sleep(0.5)
        print("Success!")
        break
    elif choice == "3":
        print("This program just a simple game of rock paper scissors in python that coded by a random person with online nickname   Nuno337 and this game is open source")
        tm.sleep(4)
        os.system('cls' if os.name == "nt" else 'clear')
    elif choice == "4":
        print("Your wins: ", a)
        print("Number of lose: ", b)
        print("Rounds played: ", r)
        print("Games finished: ", a + b)
        print("Balance: ", c)
        tm.sleep(2.5)
        os.system('cls' if os.name == "nt" else 'clear')
    else:
        print("Invalid choice!")

