# 45분 앞으로

hour, min = input().split()

hour = int(hour)
min = int(min)

if min>=45 :
    min = min - 45
else : # 45분 보다 작을때
    hour = hour-1
    if hour<0 :
        hour = 23
    min = min+60-45

print(hour, min)


