t = int(input())
ans = []

for i in range(t):
    a, b = input().split()
    a = int(a)
    b = int(b)
    ans.append(a+b)

for j in range(0, t):
    print("Case #" + str(j+1) + ": " + str(ans[j]))