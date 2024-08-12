
"""

for i in range(100):
    print(l[i % len(l)])
    
"""
def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    answer_person = { '1': 0, '2': 0, '3': 0 }
    for i in range(len(answers)):
        a = answers[i]
        if a == one[i % len(one)]:
            answer_person['1'] += 1
        if a == two[i % len(two)]:
            answer_person['2'] += 1
        if a == three[i % len(three)]:
            answer_person['3'] += 1
    max_value = max(answer_person.values())
    max_keys = sorted([key for key, value in answer_person.items() if value == max_value])
    return list(map(int, max_keys))