def solution(jobs):
    answer = 0
    len_jobs = len(jobs)
    jobs = sorted(jobs, key = lambda x : x[1])
    start = 0
    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                worktime = jobs[i][1]
                delaytime = abs(jobs[i][0] - start)
                answer += (worktime + delaytime)
                start += jobs[i][1]
                jobs.pop(i)
                break            
            
            if i == len(jobs) - 1:
                start += 1
            

    return answer // len_jobs