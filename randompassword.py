import random
ku=[]
for i in range(65,91):
    ku.append(chr(i))
for i in range(97,123):
    ku.append(chr(i))
for i in range(48, 58):
    ku.append(chr(i))

password=[]
for i in range(0,8):
    password.append(random.choice(ku))
print(password)