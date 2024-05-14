from collections import deque 

def BFS_Solution(n):
    queue = deque()
    for i in range (n):
        queue.append([i])

    filled = 1
    while(filled != n):
        qlen = len(queue)
        for i in range (qlen):
            config = queue.popleft()
            forbidden = set()

            for j, pos in enumerate(config):
                forbidden.add(pos)
                forbidden.add(pos + (filled - j))
                forbidden.add(pos - (filled - j))
            for k in range (n):
                temp_config = config[:]
                if k not in forbidden:
                    temp_config.append(k)
                    if len(temp_config) == n:
                        return temp_config
                    queue.append(temp_config)
        filled += 1
    return queue.popleft()

def printSol(lst):
    n = len(lst)
    temp = []
    for i in range(n):
        curr = ['.'] * n
        curr[lst[i]] = 'Q'
        temp.append(''.join(curr))
    for i in range (len(temp)):
        print(temp[i])

n = int(input())
printSol(BFS_Solution(n))



            