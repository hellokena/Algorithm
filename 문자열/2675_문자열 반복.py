t = int(input())
rep = []
str = []
for i in range(t):
    r,s = input().split()
    rep.append(int(r))
    str.append(s)

for i in range(t):
    for j in str[i]:
        print(j*rep[i], end = '')
    print()
