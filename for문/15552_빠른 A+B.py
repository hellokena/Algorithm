import sys
num = int(sys.stdin.readline())
ans = []

for i in range(num):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    ans.append(a+b)

for j in range(num):
    print(ans[j])
