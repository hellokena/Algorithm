n = int(input())

score = input().split()
score = [int(j) for j in score]
sum = 0

for k in score:
    sum = sum + k/max(score) * 100

print(sum/n)



