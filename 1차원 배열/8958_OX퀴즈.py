n = int(input())
sheet = []
total_score = []

for i in range(n):
    ans = input()
    sheet.append(ans)

for j in sheet:
    total = 0
    score = 0
    for k in j:
        if k == 'O':
            score += 1
            total += score
        else :
            score = 0
    total_score.append(total)

for i in total_score:
    print(int(i), sep= ' ')

