if __name__ == '__main__':
    n = int(raw_input())
    integer_list = list(map(int, raw_input().split()))
    x=tuple(integer_list)
    print(hash(x))