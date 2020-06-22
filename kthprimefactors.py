n,k=map(int,input().split())
i=3
l=[]

while(n%2==0):
    n=n//2
    l.append(2)
while(i<(int(n**0.5)+1)):
    while(n%i==0):
        n=n//i
        l.append(i)
    i+=2
if(n-1):
    l.append(n)
if(len(l)<k):
    print(-1)
else:
    print(l[k-1])
