import sys

price, laptop, l_price = map(int,sys.stdin.readline().split())
answer = 0
while (1):
    if laptop >= l_price:
        answer = -1
        break
    
    x = price / (l_price-laptop)
    answer = int(x)+1
    break
print(answer)
