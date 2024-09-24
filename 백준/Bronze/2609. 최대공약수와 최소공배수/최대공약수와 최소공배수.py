"""
최대 공약수 _ 말 그래도 공통된 약수 중에서 가장 큰 값
= 각 수의 모든 약수를 구해서 공통된 약수를 찾고 그 중에서 가장 큰 값을 반환

최소 공배수, 두 수의 공통된 배수중 가장 작은 값

두수를 각각 최소 공약수 로 나누 었을 때
6 | 24 18
    4  3
6 * 4 * 3 = 72
=> 왜 이렇게 되는 거지?
"""


def solutions():
    a, b = map(int, input().split())
    ac = []
    bc = []
    max_com = -1
    # O(n)
    for i in range(1, a + 1):
        if a % i == 0:
            ac.append(i)

    # O(n)
    for i in range(1, b + 1):
        if b % i == 0:
            bc.append(i)

    # O(n^2) => 10^8
    for item in ac:
        if item in bc:
            max_com = max(max_com, item)

    result = max_com
    for item in [a, b]:
        c = item // max_com
        result *= c

    return [max_com, result]


if __name__ == '__main__':
    for i in solutions():
        print(i)
