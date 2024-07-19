import sys
from collections import deque 

lines = 0
a = [-1] * 32
i = 0

for line in sys.stdin:
    data = str(line)
    strings = data.replace("\n", "").split(" ")

    if len(strings) == 1:
        if lines == 0 and strings[0] != 0 and i != 0:
            for j in range(len(a)):
                if a[j] == -1:
                    a[j] = '?'

            deq = deque(a)
            deq.reverse()
            print(''.join(str(x) for x in deq))
            a = [-1] * 32
            
        if strings[0] == 0:
            break
        else:
            i += 1
            lines = int(strings[0])
    else:
        if strings[0] == 'SET':
            a[int(strings[1])] = 1
            lines -= 1
        elif strings[0] == 'CLEAR':
            a[int(strings[1])] = 0
            lines -= 1
        elif strings[0] == 'AND':
            if a[int(strings[1])] == 1 and a[int(strings[2])] == 1:
                a[int(strings[1])] = 1
            elif a[int(strings[1])] == 0 or a[int(strings[2])] == 0:
                a[int(strings[1])] = 0
            else:
                a[int(strings[1])] = -1

            lines -= 1
        elif strings[0] == 'OR':
            if a[int(strings[1])] == 1 or a[int(strings[2])] == 1:
                a[int(strings[1])] = 1
            elif a[int(strings[1])] == 0 and a[int(strings[2])] == 0:
                a[int(strings[1])] = 0
            else:
                a[int(strings[1])] = -1
            
            lines -= 1
