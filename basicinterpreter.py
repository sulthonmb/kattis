#! /usr/bin/python3
import sys

variables = {}
lines_codes = {} 
sorted_lines = {}
operators = {"+", "-", "*", "/"}
conditions = ["=", ">", "<", "<>", "<=", ">="]

def handle_overflow(num):
    num = int(num) & 0xFFFFFFFF # apply 32-bit mask
    if num & 0x80000000: # check if 32nd bit is set
        num = num - 0x100000000 # convert to negative int
    return num

# param: var - array
# ex: ['A', '+', '1']
def calculate_variables(var):
    res = 0
    operator = ''

    if len(var) == 1:
        if var[0] in variables:
            res = int(variables[var[0]])
            return res
        else:
            res = int(var[0])
            return res

    for i in range(len(var)):
        if var[i] in variables:
            if operator != '':
                if operator == '+':
                    res = handle_overflow(res + int(variables[var[i]]))
                elif operator == '-':
                    res = handle_overflow(res - int(variables[var[i]]))
                elif operator == '*':
                    res = handle_overflow(res * int(variables[var[i]]))
                elif operator == '/':
                    res = handle_overflow(res / int(variables[var[i]]))
            else:
                res = int(variables[var[i]])
        elif var[i] in operators:
            operator = var[i]
        elif int(var[i]):
            if operator != '':
                if operator == '+':
                    res = handle_overflow(res + int(var[i]))
                elif operator == '-':
                    res = handle_overflow(res - int(var[i]))
                elif operator == '*':
                    res = handle_overflow(res * int(var[i]))
                elif operator == '/':
                    res = handle_overflow(res / int(var[i]))
            else:
                res = int(var[i])
        else:
            res = 0
            break

    return res

def represents_int(s):
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True

# params: conds -> array
def check_conditions(conds):
    res = None
    if len(conds) == 0:
        return False

    if len(conds) == 1:
        if represents_int(conds[0]):
            if int(conds[0]):
                return True
            else:
                return False
        elif conds[0] in variables:
            if represents_int(variables[conds[0]]):
                if int(variables[conds[0]]):
                    return True
                else:
                    return False
            else:
                return True
        elif conds[0] not in variables:
            return False
        else:
            return False

    for i in range(len(conds)):
        operands = [0, 0]
        res_operands = None

        if conds[i] in conditions:
            if represents_int(conds[i-1]):
                operands[0] = int(conds[i-1])
            elif conds[i-1] in variables:
                operands[0] = int(variables[conds[i-1]])
            else:
                return False

            if represents_int(conds[i+1]):
                operands[1] = int(conds[i+1])
            elif conds[i+1] in variables:
                operands[1] = int(variables[conds[i+1]])
            else:
                return False

            if conds[i] == '=':
                if res == None:
                    res = operands[0] == operands[1]
                else:
                    res = res and (operands[0] == operands[1])
                
            elif conds[i] == '>':
                if res == None:
                    res = operands[0] > operands[1]
                else:
                    res = res and (operands[0] > operands[1])
                
            elif conds[i] == '<':
                if res == None:
                    res = operands[0] < operands[1]
                else:
                    res = res and (operands[0] < operands[1])
                
            elif conds[i] == '>=':
                if res == None:
                    res = operands[0] >= operands[1]
                else:
                    res = res and (operands[0] >= operands[1])
                
            elif conds[i] == '<=':
                if res == None:
                    res = operands[0] <= operands[1]
                else:
                    res = res and (operands[0] <= operands[1])
                
            elif conds[i] == '<>':
                if res == None:
                    res = operands[0] != operands[1]
                else:
                    res = res and (operands[0] != operands[1])
    return res

for line in sys.stdin:
    data = str(line).replace("\n", "").split(' ')
    lines_codes[int(data[0])] = data[1:]

sorted_lines = sorted(lines_codes)

z = 0
while z <= len(sorted_lines)-1:
    code = lines_codes[sorted_lines[z]]
    # print(code)

    if code[0] == 'END':
        break

    if code[0] == 'GOTO':
        for j in range(len(sorted_lines)):
            if sorted_lines[j] == int(code[1]):
                z = j
                continue

    if code[0] == 'LET':
        for i in range(1, len(code)):
            if code[i] == '=':
                formula = code[i+1:]
                variables[code[i-1]] = calculate_variables(formula)
        
        z += 1
        continue
            
    elif code[0] == 'PRINTLN':
        if '"' in list(code[1]):
            string = code[1:]
            print(" ".join(string).replace('"', ''))
        else:
            res_calc = calculate_variables(code[1:])
            print(res_calc)
        z += 1
        continue
    
    elif code[0] == "PRINT":
        if '"' in list(code[1]):
            string = code[1:]
            print(" ".join(string).replace('"', ''), end="")
        else:
            res_calc = calculate_variables(code[1:])
            print(res_calc, end="")

        z += 1
        continue

    elif code[0] == 'IF':
        conds = []
        for i in range(1, len(code)):
            conds.append(code[i])
            if code[i] == 'THEN':
                conds = conds[:-1]
                result_conds = check_conditions(conds)

                if result_conds and code[i+1] == 'GOTO':
                    for j in range(len(sorted_lines)):
                        if sorted_lines[j] == int(code[i+2]):
                            z = j-1
                            continue

        z += 1
        continue
