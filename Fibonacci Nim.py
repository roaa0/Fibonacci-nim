#Fibonacci Nim
#display a random number
import random
n=coins=random.randint(2,100)
player=1
x=100
print("the number of coins is now ", coins)
while True :
    print("player" ,player ," take number of coins :" )

    while True:
        i = int(input())
                                                         # the first player can't take all the coins
        if 2*x>=i and i<=coins and i!=n and i>0:         # it is not allowed to take more than twice of the previous move and -ve number
            break
        else:
            print("illegal move")
    x=i
    coins=coins-i
    print("the number of coins is now " , coins)

    if coins==0:                                         #check the condition of wining
        print("player", player ,"wins")
        break

    if player==1 :                                       #changing turns
        player=2
    else:
        player=1

print("game is over")
