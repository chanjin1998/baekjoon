N = int(input())
i = 666
cnt = 0
while(1):
    if '666' in str(i):
        cnt +=1
    if cnt == N:
        print(i)
        break
    i+=1
