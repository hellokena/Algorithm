first_n = int(input())
cycle = 0
new = -1

n = first_n

while first_n != new:
    #if n//10 > 0:
    first = n//10
    #else : first = 0
    second = n%10
    sum = first + second
    new = 10*second + sum%10
    n = new
    cycle = cycle + 1
print(cycle)






