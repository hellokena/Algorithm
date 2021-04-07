white = 0
for i in range(8):
    graph = input()
    if i%2 == 0: # 짝수
        for j1 in range(0, 8, 2):
            if graph[j1] == 'F':
                white += 1
    else:
        for j2 in range(1,8,2):
            if graph[j2] == 'F':
                white += 1
#0번째 줄은 짝수번호[0,2,4,6,8]
#1번째 줄은 홀수번호[1, 3, 5,7]
print(white)
