"""
1. 아이디어

10/1, 10/2, 10/3 ...

조합 아닌가?
n 개 중에 1개 선택 하는 모든 경우의 수 출력
=> 반복문 돌면서 계산 하면서 신맛이 가장 적은 케이스 를 찾는다.

"""
from itertools import combinations


def solutions():
    n = int(input())
    foods = []
    for i in range(1, n + 1):
        sin, ssun = map(int, input().split())
        foods.append((i, sin, ssun))
    differ = 1000000000
    for i in range(1, n + 1):  # 무조건 재료는 하나 정도는 사용 해야 하기 때문에 1부터 시작
        # 재료 i 개를 사용 해서 만들 수 있는 모든 조합 산출
        for food_combi in list(combinations(foods, i)):
            sin_flavor = 1
            ssun_flavor = 0
            for food in food_combi:
                sin_flavor *= food[1]
                ssun_flavor += food[2]
            differ = min(abs(sin_flavor - ssun_flavor), differ)

    return differ


if __name__ == '__main__':
    print(solutions())
