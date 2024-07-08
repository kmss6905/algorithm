"""
 00(1) 01(2) 02(3) 03(4)
 10(2) 11(2) 12(3) 13(4)(시작)
 20(3) 21(3) 22(3) 23(4)
 30(4) 31(4) 32(4) 33(4)(끝)

4 3 3 3 4 4 4 4 4

00 01 02 03 | 10 11 12 13 

7 -> 몇 번 째 로우에 몇번 째 칸 ? ->  1 = 7/4(몫), 3 = 8%4(나머지) -> [1][3]
몫 2 -> 
 
 14 / 4 => 3
 14 % 4 => 2

"""

def solution(n, left, right):
    answer = []    
    start = (left // n, left % n)
    end = (right // n, right % n)
    # print(start, end)
    for i in range(start[0], end[0]+1):
        for j in range(n):
            if i == start[0] and j < start[1]:
                continue
            # print(i, j)
            answer.append(max(i, j) + 1)
            if (i, j) == end: # 끝에 도달
                break
    # print(answer)
    return answer