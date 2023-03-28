#stone paper scissor game developed by Aditya Pandey
import random
print("\t\t\tSTONE  PAPER  SCISSOR\n\t\t    Developed by :- Aditya Pandey\n---> You have 5 chances")

print("---> Choices : --\n       • s for Stone\n       • p for Paper\n       • S for Scissor")
print("\t\t\tSTART THE GAME")
You_lost=0
You_win=0
chances=10
no_of_chances=0

while(no_of_chances<chances):
  box=['Stone','Paper','Scissor']
  a=random.choice(box )
  z=chances-no_of_chances
  print(f"\n{z} Chances Left")
  b=input("Your Choice : ")
  print(f"Computer's Choice : {a}")
  if a=='Stone' and b=='p':
    print("•••You Won•••")
    You_win=You_win + 1
    print(f"Your Points : {You_win}\nComputer's Points : {You_lost}")
  elif a=='Stone' and b=='s':
    print("•••Draw•••")
  elif a=='Stone' and b=='S':
    print("•••You Lost•••")
    You_lost=You_lost+1
    print(f"Your Points : {You_win}\nComputer's Points : {You_lost}")
  elif a=='Paper' and b=='p':
    print("•••Draw•••")
  elif a=='Paper' and b=='s':
    print("•••You Lost•••")
    You_lost=You_lost+1
    print(f"Your Points : {You_win}\nComputer's Points : {You_lost}")
  elif a=='Paper' and b=='S':
    print("•••You Won•••")
    You_win=You_win+1
    print(f"Your Points : {You_win}\nComputer's Points : {You_lost}")
  elif a=='Scissor' and b=='p':
    print("•••You Lost•••")
    You_lost=You_lost+1
    print(f"Your Points : {You_win}\nComputer's Points : {You_lost}")
  elif a=='Scissor' and b=='s':
    print("•••You Won•••")
    You_win=You_win+1
    print(f"Your Points : {You_win}\nComputer's Points : {You_lost}")
  elif a=='Scissor' and b=='S':
    print("•••Draw•••")
  else:
    print("Invalid Input")
  no_of_chances=no_of_chances+1
if You_win>You_lost:
  print("\t\t\tYou Won the match")
elif You_win==You_lost:
  print("\t\t\tMatch Tie")
else:
 print("\t\t\tComputer won the match")
print("\t\t\t\tGAME END")
print("\t\t\tHope! you enjoyed it")
