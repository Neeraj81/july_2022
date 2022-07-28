if __name__ == '__main__':
    d=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        d.append([name, score])
    x=sorted(set([x for name, x in d]))[1]
    n=[]
    for name, score in d:
        if score==x:
            n.append(name)
    n.sort()
    print("\n".join(n))
