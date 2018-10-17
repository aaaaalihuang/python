def move(n,a,b,c):#n为个数，a为原始，b为辅助，c为目的
    global count
    if n==1:
        print(f"{a}-->{c}")
        count+=1
    #
    # elif n==2:
    #     print(f"{a}-->{b}")
    #     count += 1
    #     print(f"{a}-->{c}")
    #     count += 1
    #     print(f"{b}-->{c}")
    #     count += 1
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)



count=0
move(3,"a","b","c")
print(count)