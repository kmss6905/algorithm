"""
10^6
4 * 10^6

| 1 | 2 | 3 | 99 |
| 5 | 6 | 4 | 100 |
| 4 | 100 | 2 | 1 |

각 최선의 값 : 99 + 6 + 4 = 109
실제 최대 값 : 100 + 100 + 3 = 203

다 일일히 더해보기 전까지는 모르나?

미리 그 전까지의 결과를 저장해놓는다.

"""
def solution(land):
    for i in range(1,len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[len(land)-1])