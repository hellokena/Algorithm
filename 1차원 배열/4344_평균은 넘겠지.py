
c = int(input())

for i in range(c):
    sum = 0
    num = 0
    stu = input().split()
    stu = [int(a) for a in stu]

    for j in range(1, len(stu)):
        sum += stu[j]
    avg = sum/(len(stu)-1) # 평균
    for k in range(1, len(stu)):
        if stu[k] > avg:
            num += 1
    #print(round(((num/(len(stu)-1))*100,3)) , "%")
    print('%0.3f' % round((num/(len(stu)-1))*100, 3) + "%")

