score1=0
score2=0
while True :
    player1=input()
    if player1 not in ["rock,paper,sciosser"]:
        print("please enter the rock,paper,sciosser")
        player1=input()

    player2=input()
    if player2 not in ["rock,paper,sciosser"]:
        print("please enter the rock,paper,sciosser")
        player2=input()

        break

    for i in range(0,4):
   
        if player1=="rock" and player2=="rock":
         print("there is no winner")
        elif player1=="rock" and player2=="paper":
         print("the winner is player2")
         score2=score2+1
        elif player1=="rock" and player2=="sciosser":
         print("the winner is player1")
         score1=score1+1
        elif player1=="paper" and player2=="rock":
          print("the winner is player1")
          score1=score1+1
        elif player1=="paper" and player2=="paper":
         print("there is no winner")
        elif player1=="paper" and player2=="sciosser":
         print("the winner is player2")
         score2=score2+1
        elif player1=="sciosser" and player2=="rock":
          print("the winner is player2")
          score2=score2+1
        elif player1=="sciosser" and player2=="paper":
          print("the winner is player1")
          score1=score1+1
        elif player1=="sciosser" and player2=="sciosser":
          print("there is no winner")

if score1>score2:
    print("THE WINNER PLAYER 1")
elif score1<score2:
    print("THE WINNER PLAYER 2")
else:
    print("THERE IS NOT WINNER")


