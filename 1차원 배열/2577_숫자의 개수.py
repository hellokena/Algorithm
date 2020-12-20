a = int(input())
b = int(input())
c = int(input())

num = str(a*b*c)

for i in range(10):
    num = str(num)
    print(num.count(str(i)))

