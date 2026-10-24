#寻找素数

m,n=map(int,input("请输入两个整数，以空格分隔：").split())
for i in range(m,n+1):
    t=0
    for j in range(1, i+1):
        if i % j==0:
            t+=1
            if t>2:
                break
    if t==2:
        print(i,end=" ")
            