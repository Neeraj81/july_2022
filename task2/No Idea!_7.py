n, m= input().split()
count=0
a=list(map(int, input().split()))
A=set(map(int, input().split()))
B=set(map(int, input().split()))
for i in a:
    if i in A:
        count+=1
    elif i in B:
        count-=1
print(count)