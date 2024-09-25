# 제한 시간 2초
"""
1. 아이디어 : 단순 구현 ? 어차피 2초 ?
2. 구현
# 1부터 1000 까지 반복
answer = [0] # 나중에 인덱스 계산 편하게 하기 위해서
for  i 1 ~ 1000:
 for _ in range(i):
  answer.append(i);
  if len(answer) > 1000:
    break

answer.insert(0, 0)
sum(answer[a:b+1])

3. 시간복잡도, 최대 길이가 b 까지만 입력되기 때문에 O(b) 이다
b 의 최대 1000
따라서 O(N), N = 1000

"""


def solutions():
    a, b = map(int, input().split())
    answer = [0]
    flag = False
    for i in range(1, 1001):
        for _ in range(i):
            answer.append(i)
            if len(answer) > b:
                flag = True
                break
        # 더 이상 추가할 필요가 없기 때문에 중단
        if flag:
            break
    return sum(answer[a:b+1])


if __name__ == '__main__':
    print(solutions())
