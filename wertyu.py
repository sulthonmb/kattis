#! /usr/bin/python3
import sys

keyboards = [
    ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="],
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
]

for line in sys.stdin:
    data = str(line)
    strings = list(data)
    ans = ''
    for string in strings:
        found = False
        for i in range(len(keyboards)):
            for j in range(len(keyboards[i])):
                if keyboards[i][j] == string:
                    if j == 0:
                        found = True
                        ans += keyboards[i][j+1]
                    else:
                        found = True
                        ans += keyboards[i][j-1]

        if found == False:
            ans += ' '
    
    print(ans)