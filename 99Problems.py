
if __name__ == '__main__':
    i = int(input())
    if (i < 100):
        cint = 99
    else:
        if (i % 100 < 49):
            cint = i - (i % 100 + 1)
        else:
            cint = (99 - (i % 100)) + i
    print(cint)