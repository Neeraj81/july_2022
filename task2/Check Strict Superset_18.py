a=set(map(int, input().split()))
n=int(input())
b=set(map(int, input().split()))
c=set(map(int, input().split()))
if b.issubset(a) and c.issubset(a):
    print('True')
else:
    print('False')