N, M, Q = list(map(int, input().split()))
solved_num_list = [0 for _ in range(M)]
solved_problem_list = [[] for _ in range(N)]

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if len(query) == 2:
        score = 0
        for problem in solved_problem_list[query[1]-1]:
            score += N - solved_num_list[problem]
        print(score)
    else:
        n = query[1]-1
        m = query[2]-1
        solved_num_list[m] +=1
        solved_problem_list[n].append(m)
