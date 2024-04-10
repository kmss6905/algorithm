cnt = 0
while True:
    try:
        print(input())
        cnt += 1
        if cnt == 100:
            break
    except:
        break