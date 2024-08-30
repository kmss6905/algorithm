from collections import defaultdict
def solution(players, callings):
    answer = []
    pi = defaultdict(int)
    for index, player in enumerate(players):
        pi[player] = index
    
    for calling in callings:
        current_index = pi[calling]
        players[current_index] = players[current_index - 1]
        players[current_index-1] = calling
        
        pi[calling] -= 1
        pi[players[current_index]] += 1
        
        
    return players