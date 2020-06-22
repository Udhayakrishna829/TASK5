l=list(map(int,input().split()))
k=int(input())
s=0
for i in l:
    if(i%k>((k//2)+1)):
        s+=(k-(i%k))
    else:
        s+=(i%k)
print(s)
