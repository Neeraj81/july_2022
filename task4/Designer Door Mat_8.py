x, y=input().split()
for i in range(1, int(int(x)-1), 2):
    X=int(int(x)/2)-int((i+1)/2)+1
    print("---"*X+".|."*i+"---"*X)
A=int((int(y)-7)/2)
print(A*"-"+"WELCOME"+A*"-")
for i in range(int(int(x)-2), 0, -2):
    X=int(int(x)/2)-int((i+1)/2)+1
    print("---"*X+".|."*i+"---"*X)