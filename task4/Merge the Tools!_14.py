#import textwrap

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        res = ''
        for c in string[i : i+k]:
            if (c not in res):
                res+=c
        print(res)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)