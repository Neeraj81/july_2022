n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(N):
    l=input().split()
    if l[0]=='pop':
        s.pop()
    if l[0]=='discard':
        s.discard(int(l[1]))
    if l[0]=='remove':
        s.remove(int(l[1]))

print(sum(s))