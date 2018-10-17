from datetime import datetime
now=datetime.now()
print(now.strftime("程序开始，现在是{0:%H}时{0:%M}分{0:%S}秒".format(now)))

n=0
for i in range(0,10000):
    for i in range(0,10000):
        n+=1

now2=datetime.now()
print(now2.strftime("程序结束，现在是{0:%H}时{0:%M}分{0:%S}秒".format(now2)))
h=now2.hour-now.hour
m=now2.minute-now.minute
s=now2.second-now.second
print(f"共运行{h}小时{m}分{s}秒")
print(n)