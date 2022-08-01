if __name__ == '__main__':
    s = list(input())
    if any(a.isalnum() for a in s):
        print("True")
    else:
        print("False")
    if any(a.isalpha() for a in s):
        print("True")
    else:
        print("False")
    if any(a.isdigit() for a in s):
        print("True")
    else:
        print("False")
    if any(a.islower() for a in s):
        print("True")
    else:
        print("False")
    if any(a.isupper() for a in s):
        print("True")
    else:
        print("False")