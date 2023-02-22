time = 0
pcount = 0
tflag = []
while (1):
    run = list(input().split())
    if int(run[0]) == -1:
        print(pcount, time)
        exit(0)
    elif run[2] == "right":
        time += int(run[0])
        pcount += 1
        if tflag.count(run[1]) > 0:
            time += 20 * tflag.count(run[1])
    else:
        tflag.append(run[1])
