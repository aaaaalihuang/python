import random
def creatBirthday(n):
    birthdays=[]

    for i in range(0,n):
        birthdays.append(random.randint(1,366))

    birthdays.sort()
    return birthdays


n=int(input("请输入人数"))
m=int(input("请输入模拟次数"))
# a=creatBirthday(n)

count=0
for j in range(0,m):
    a=creatBirthday(n)
    for i in range(0,n):

        if i<n-1 and a[i]==a[i+1]:
            count=count+1
            break
        else:
            pass

print(count,count/m)