import random

count1 = 0
count2 = 0

for i in range(0,100000):
    ccc = [1, 2, 3]
    car=random.randint(1,3)

    for i in (1,2,3):
        if car==i:
            ccc.pop(i-1)
            break

    goat1=random.choice(ccc)
    goat2=6-goat1-car
    d=[]
    d.append(goat1)
    d.append(goat2)

    player=random.randint(1,3)
    host=5
    if car==player:
        host=random.choice(d)
    else:
        host=6-player-car


    if car==player:
        count1+=1

    if (6-host-player)==car:
        count2+=1



print(f"不换猜中的次数为{count1},换了猜中的次数为{count2}")