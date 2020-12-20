arr = []
ans_arr = []
for i in range(10):
    num = int(input())
    arr.append(num)

for i in range(10):
    ans = arr[i]%42
    ans_arr.append(ans)

ans_arr = set(ans_arr)
print(len(ans_arr))