# LinkedList
import sys

i = 0
total_test_case = 0
result = []
ans = []
cursor = 'end'
is_home_first = False

for line in sys.stdin:
    data = str(line)

    if i == 0:
        total_test_case = int(data)
        i += 1
        continue

    if total_test_case > 0:
        strings = list(data.replace("\n",""))

        for j in range(len(strings)):
            string = strings[j]

            if string == '[':
                cursor = 'home'

                if len(result) != 0:
                    is_home_first = False

                    z = j+1
                    k = None
                    while z < len(strings):
                        if strings[z] == ']':
                            k = z
                            home_string = strings[j+1:k]
                            home_string.reverse()
                            strings[j+1:k] = home_string
                            break
                        z += 1
                    
                else:
                    is_home_first = True
            elif string == ']':
                cursor = 'end'
            elif string == '<' and cursor == 'end' and len(result) > 0:
                result.pop()
            else:
                if cursor == 'end':
                    result.append(string)
                elif cursor == 'home':
                    if is_home_first:
                        if string == '<' and len(result) > 0:
                            result.pop()
                        else:
                            result.append(string)    
                    else:
                        result.reverse()
                        result.append(string)
                        result.reverse()                

        for res in result:
            if res == '<' and len(ans) > 0:
                ans.pop()
            elif res != '<':
                ans.append(res)

        print("".join(ans))
        result = []
        ans = []
        total_test_case -= 1