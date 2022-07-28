a=int(input())
aa=set(map(int, input().split()))
b=int(input())
bb=set(map(int, input().split()))
aaa=aa.difference(bb)
bbb=bb.difference(aa)
aaa.update(bbb)
for i in sorted(aaa):
    print(i)