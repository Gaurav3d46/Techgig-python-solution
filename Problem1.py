a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=[]
for j in range(a):
    s=c[j]//b[j]
    d.append(s)
d.sort()
print(d[0])
