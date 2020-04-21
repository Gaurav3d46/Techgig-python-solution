T=int(input())
for i in range(T):
    count=0
    N=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    c=0
    for i in range(N):
        for j in range(c,N):
            if (A[i]>B[j]):
                c=j+1
                count+=1
                break
        
    print(count)
