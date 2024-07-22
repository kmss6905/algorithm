# 5^5 < 10 ^ 5
# combination 사용하지 않고
# def solution(word):
#     w = ['A', 'E', 'I', 'O', 'U']
#     # 최대 5단어
#     # 4 글자 ? -> 1글자로 만들수있는 경우의 수 + 2글자로 만들 수 있는 경우의수 + 3 ..
#     # AAAE -> A AA AAA AAAA AAAAA AAAAE AAAAAI ... 
    
    
    
#     answer = 0
#     return answer

def solution(word):
    answer = 0
    word_list = []
    words = 'AEIOU'
    
    def dfs(cnt, w):
        if cnt == 5: # 만들 수 있는 단어의 최대 길이는 5이다.
            return 
        for i in range(len(words)):
            word_list.append(w + words[i]) # 순서대로 들어가게 된다.
            dfs(cnt+1, w + words[i])
            
    dfs(0,"")
    
    return word_list.index(word)+1