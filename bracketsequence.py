import sys

stacks = []
i = 0
MOD = 10**9 + 7

for line in sys.stdin:
    if i == 0:
        i += 1
        continue
    
    toggle_plus = True
    data = str(line).replace("\n", "").split(" ")
    
    for val in data:
        if val == '(':
            toggle_plus = not toggle_plus

        if val == ')':
            if toggle_plus:
                count = 0
            else:
                count = 1

            while i <= len(stacks):
                pop_val = stacks.pop()
                if pop_val == '(':
                    break
                else:
                    if toggle_plus:
                        count = (count + int(pop_val)) % MOD
                    else:
                        count = (count * int(pop_val)) % MOD

            toggle_plus = not toggle_plus
            stacks.append(str(count % MOD))
        else:
            stacks.append(val)

        if toggle_plus:
            ans = 0
        else:
            ans = 1

    for stack in stacks:
        if stack != '(' and stack != ')':
            if toggle_plus:
                ans = (ans + int(stack)) % MOD
            else:
                ans = (ans * int(stack)) % MOD
    
    print(ans % MOD)
    
    
