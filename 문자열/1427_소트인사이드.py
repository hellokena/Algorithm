import sys
n = list(map(int, str(sys.stdin.readline().rstrip())))
n.sort(reverse=True)
print(''.join(map(str, n)))
