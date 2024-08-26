from collections import deque

def solution(cards1, cards2, goal):
    answer = "Yes"
    """
    기존 python list 의 pop(idx)를 사용해도 되지만, pop(0) 의 경우 비워진 인덱스를 채우기 위해서 모든 원소가 왼쪽으로 한칸씩 이동해야하는 연산이 발생하여 배열의 길이만큼의 시간 복잡도가 발생합니다.
    하지만 deque 의 경우에는 이중연결리스트로 작성되어있기 때문에 O(1) 의 시간복잡도로 원소를 제거할 수 있습니다.
    """
    c1 = deque(cards1)
    c2 = deque(cards2)
    """
    goal 의 길이 즉, 만들려고 하는 단어의 길이가 N
    O(N)의 시간복잡도를 가집니다.
    """
    for word in goal:
        """
        python 의 deque 는 linkedlist 로 구현되어있습니다.
        따라서 linkedlist 첫번 째 원소를 제거 했을 경우 O(1) 시간 복잡도가 소요됩니다.
        그렇기 때문에 for 문 안의 로직은 모두 O(1) 시간 복잡도를 가집니다.
        """
        if c1 and c1[0] == word:
            c1.popleft()
            continue
        
        if c2 and c2[0] == word:
            c2.popleft()
            continue
        answer = "No"
    return answer