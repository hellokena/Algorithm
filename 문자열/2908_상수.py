f,s = input().split()
reverse_f = int(f[::-1])
reverse_s = int(s[::-1])

if reverse_f > reverse_s :
    print(reverse_f)
else: print(reverse_s)