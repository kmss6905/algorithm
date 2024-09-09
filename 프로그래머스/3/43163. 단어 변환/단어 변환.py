from collections import deque

def solution(begin, target, words):
    answer = 0
    words.append(begin)
    if target not in words:
        return 0
    
    graph = {}
    visited = {}
    for word in words:
        graph[word] = []
        visited[word] = False
    
    for key in graph.keys():
        for word in words:
            cnt = 0
            if key != word:
                for i in range(len(key)):
                    if key[i] == word[i]:
                        cnt += 1
                if cnt == len(key) - 1:
                    graph[key].append(word)

    q = deque()
    q.append((0, begin))    
    while q:
        cnt, current_word = q.popleft()
        if current_word == target:
            answer = cnt
            break
        for next_word in graph[current_word]:
            if not visited[next_word]:
                q.append((cnt+1, next_word))
                visited[next_word] = True
    return answer