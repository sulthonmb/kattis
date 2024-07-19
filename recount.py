#! /usr/bin/python3
import sys

candidates = {}

for line in sys.stdin:
    data = str(line).replace("\n", "")
    
    if (data == '***'):
        count = 0
        ans = max(candidates, key=candidates.get)

        for i in candidates:
            if candidates[i] == candidates[ans]:
                count += 1
        
        if count > 1:
            print("Runoff!")
        else:
            print(ans)
        
        break

    if data not in candidates:
        candidates[data] = 1
    else:
        candidates[data] += 1
    
