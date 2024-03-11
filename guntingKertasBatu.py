model1 = "Gunting" 
model2 = "Kertas" 
model3 = "Batu" 

player1 = (input("Player 1 memasang model apa : "))
player2 = (input("Player 2 memasang model apa : "))

status1 = "Draw"
status2 = "Win"

if player1 == model1.lower() and player2 == model1.lower():
    print(status1)
elif player1 == model1.lower() and player2 == model2.lower():
    print(player1, status2)
elif player1 == model1.lower() and player2 == model3.lower():
    print(player2, status2)
    
elif player1 == model2.lower() and player2 == model2.lower():
    print(status1)
elif player1 == model2.lower() and player2 == model1.lower():
    print(player2, status2)
elif player1 == model2.lower() and player2 == model3.lower():
    print(player2, status2)
    
elif player1 == model3.lower() and player2 == model3.lower():
    print(status1)
elif player1 == model3.lower() and player2 == model1.lower():
    print(player1, status2)
else:
    print(player2, status2)    
