for i in range(int(input())):
    n=input()
    a=set(map(int, input().split()))
    nn=input()
    b=set(map(int, input().split()))
    print(a.issubset(b))