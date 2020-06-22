n=int(input())
i=2
l=[]
while(i<(int(n**0.5)+1)):
    while(n%i==0):
        n=n//i
        l.append(i)
    i+=1
if(n-1):
    l.append(n)
for i in sorted(set(l)):
    print(i,l.count(i))
