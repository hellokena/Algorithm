
import sys

def solution(n):
    array = []
    for _ in range(n):
        array.append(int(sys.stdin.readline().rstrip()))
    array.sort()
    for i in array:
        print(i)

n = int(sys.stdin.readline().rstrip()) # 구하고자 하는 수
solution(n)
