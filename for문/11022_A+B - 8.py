t = int(input())
ans = []

for i in range(t):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print("Case #" + str(i+1) + str(": ") + str(a) + " + " + str(b) + " = " + str(a+b))
