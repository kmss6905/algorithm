def solution(jobs):
    answer = 0
    jobs_num = len(jobs)
    jobs = sorted(jobs, key = lambda x : x[1]) # ex, [[2, 6], [1, 9]]
    start = 0 # start = 3
    
    # 대기시간 + 작업시간
    while len(jobs) != 0 :
        for i in range (len(jobs)):
            # 작업 요청 시점
            if jobs[i][0] <= start: # 2 < 3 -> 어? 이미 요청이 됬다
                start += jobs[i][1]  # 3 + 6 -> 9
                answer += abs(jobs[i][0] - start) # 2 - 9
                jobs.pop(i)
                break;

            if i == len(jobs) -1 : # 마지막 도착시, start += 1
                start +=1                

    return answer // jobs_num