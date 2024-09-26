import math

def solutions():
    m = int(input())
    n = int(input())
    sosus = []
    
    for num in range(m, n + 1):
        if num < 2:
            continue  # 2 미만의 수는 소수가 아님

        is_sosu = True
        for i in range(2, int(math.sqrt(num)) + 1):  # 제곱근까지만 확인
            if num % i == 0:
                is_sosu = False
                break

        if is_sosu:
            sosus.append(num)

    if len(sosus) == 0:
        print(-1)
    else:
        print(sum(sosus))
        print(sosus[0])


if __name__ == '__main__':
    solutions()
