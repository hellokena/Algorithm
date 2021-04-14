import sys
s = sys.stdin.readline().rstrip().split('-')
result=''
for i in s:
    result += i[0]
print(result)
