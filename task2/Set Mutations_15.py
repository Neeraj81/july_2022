n=input()
a=set(map(int, input().split()))
for i in range(int(input())):
    l=input().split()
    if l[0]=="intersection_update":
        a.intersection_update(set(map(int, input().split())))
    elif l[0]=="update":
        a.update(set(map(int, input().split())))
    elif l[0]=="symmetric_difference_update":
        a.symmetric_difference_update(set(map(int, input().split())))
    elif l[0]=="difference_update":
        a.difference_update(set(map(int, input().split())))
print(sum(a))