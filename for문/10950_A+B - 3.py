ans = []

num = int(input())

for i in range(num):
    # a, b = map(int, input().split())
    first, second = input().split()
    first = int(first)
    second = int(second)
    ans.append(first+second)

for j in range(num):
    print(ans[j])

