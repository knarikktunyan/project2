import random
d1=random.randint(1,6)
d2=random.randint(1,6)
tot=d1+d2
print(tot)

if tot==7 or tot==11:
    print("You won")
elif tot==2 or tot==3 or tot==12:
    print("You lose")
else: 
    goal = tot
    print("Your goal is " + str(goal))
    while True:
        tot1 = random.randint(1, 6) + random.randint(1, 6)
        print("Your roll is " + str(tot1))
        if tot1 == 7:
            print("You lose")
            break
        elif tot1 == goal:
            print("You win")
            break
        

