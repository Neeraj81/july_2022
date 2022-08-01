def print_formatted(number):
    lenth = len(bin(number))-2
    for i in range(1,number+1):
        o = oct(i).split('o')
        h = hex(i).split('x')
        a=h[1].upper()
        b = bin(i).split('b')
        print(str(i).rjust(lenth), o[1].rjust(lenth), a.rjust(lenth), b[1].rjust(lenth))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)