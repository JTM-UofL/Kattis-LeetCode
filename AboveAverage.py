for i in range(int(input())):
    num = list(map(int, input().split()))
    num_students = float(num[0])
    num.pop(0)
    mean = sum(num) / len(num)
    student = 0.00
    for number in num:
        if number > mean:
            student += 1
    print("{:.3f}%".format((student / num_students) * 100))
