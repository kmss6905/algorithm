def solution(array, commands):
    answer = []
    for i in commands:
        new_array = sorted(array[i[0]-1:i[1]]) # O(nlogn)
        answer.append(new_array[i[2]-1]) # O(1)
    return answer