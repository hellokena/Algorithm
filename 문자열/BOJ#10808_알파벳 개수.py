import sys
s = sys.stdin.readline().rstrip()
array = [0]*26
for i in s:
    array[ord(i)-97] += 1
print(' '.join(map(str, array)))
