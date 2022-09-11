import sys
n, k = map(int, input().split())
money = [k]
count = 0

for _ in range(n) :
    a = int(sys.stdin.readline())
    money.append(a)
  
while True :
    money.sort()
    i = money.index(k)
    if money.count(k) >= 2 :
        print(count + 1)
        break 
    money[i] = money[i] - money[i-1]
    k = k - money[i-1]

    count += 1
