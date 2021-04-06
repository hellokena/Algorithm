s = input().upper()
dic = {}
for i in s:
  if i in dic.keys():
    dic[i] += 1
  else:
    dic[i] = 1
max_v = max(dic.values())
result = ''
for key, value in dic.items():
  if value == max_v:
    result += key
if len(result) == 1:
  print(result[0])
else:
  print('?')



