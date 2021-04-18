
import sys

def solution(n):
    array = []
    for _ in range(n):
        array.append(list(map(int, sys.stdin.readline().rstrip().split())))
    array.sort()
    for i in array:
        print(i[0], i[1])

n = int(sys.stdin.readline().rstrip()) # 구하고자 하는 수
solution(n)
