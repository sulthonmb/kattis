#! /usr/bin/python3
import sys
 
characters = []
mapping_chars = {}
mapping_value_chars = {}
i = 0
result = True


for line in sys.stdin:
    data = str(line)
    if (i == 0):
        characters = list(data)
        characters.pop()
        i += 1
    else:
        strings = data.split(' ')
        if (len(strings) != len(characters)):   
            result = False         
            break
        
        for index, string in enumerate(strings):
            if string not in mapping_chars and characters[index] not in mapping_value_chars:
                mapping_chars[string] = characters[index]
                mapping_value_chars[characters[index]] = string
            else:
                try:
                    if mapping_chars[string] != mapping_chars[mapping_value_chars[characters[index]]]:
                        result = False
                        break
                except:
                    result = False
                    break

print(result)