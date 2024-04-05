from collections import deque

def solution(begin, target, words):
    answer = 0
    
    # 무조건 변환할 수 없는 경우
    if target not in words:
        return answer
    
    # 그래프 구현
    graph = {}
    words.append(begin)
    word_len = len(words[0])
    for w in words:
        if w not in graph:
            graph[w] = []
        
        for other_word in words:
            diff_alpha_cnt = 0
            if w != other_word:
                for i in range(word_len):
                    if w[i] != other_word[i]:
                        diff_alpha_cnt += 1
            if diff_alpha_cnt == 1:
                graph[w].append(other_word)
                
    # 그래프 탐색
    visited = []
    queue = deque()
    queue.append((begin, 0))
    visited.append(begin)
    while queue:
        cur_word, distance = queue.popleft()
        for next_node in graph[cur_word]:
            if next_node not in visited:
                distance += 1
                visited.append(next_node)
                queue.append((next_node, distance))
                if next_node == target:
                    return distance
        
    return answer