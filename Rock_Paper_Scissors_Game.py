score1=0
score2=0
i=0
while i<3:
    i=i+1
    print("please enter the rock,paper or sciosser")
    player1=input()
    player2=input()
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
    print (score1,":",score2, "THE WINNER PLAYER")
elif score1<score2:
    print(score2,":",score1,"THE WINNER PLAYER 2")
else:
    print( score2,":",score1,"THERE IS NOT WINNER")


