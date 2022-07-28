n=int(input())
s=list(map(int, input().split()))
ss = set(s)
print (((sum(ss)*n)-(sum(s)))//(n-1))