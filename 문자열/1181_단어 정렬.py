import sys
n = int(sys.stdin.readline().rstrip())
array = []
for i in range(n):
    word = sys.stdin.readline().rstrip()
    if word not in array: # 같은 것 제외
        array.append(word)
array.sort() # 알파벳 순으로 1차 정렬
array.sort(key=lambda x: len(x)) # 길이로 1차 정렬
for i in array:
    print(i)
