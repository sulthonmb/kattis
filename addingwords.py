#! /usr/bin/python3
import sys

variables = {}
variables_value = {}
operators = ['+', '-', '=']
result_operator = '='

for line in sys.stdin:
    data = str(line)
    strings = data.replace("\n","").strip().split(' ')
    ans = []

    for index_string in range(len(strings)):
        if strings[index_string] == 'def':
            if strings[index_string+1].lower() in variables:
                if int(variables[strings[index_string+1].lower()]) in variables_value:
                    del variables_value[int(variables[strings[index_string+1].lower()])]
                del variables[strings[index_string+1].lower()]

            variables[strings[index_string+1].lower()] = int(strings[index_string+2].replace("\n", ""))
            variables_value[int(strings[index_string+2].replace("\n", ""))] = strings[index_string+1].lower()
        
        if strings[index_string] == 'clear':
            variables = {}
            variables_value = {}

        if strings[index_string] == 'calc':
            value = 0
            unknown = False
            operator = ''

            for index_calc in range(len(strings)):
                if strings[index_calc] == 'calc':
                    continue

                # Calculation
                if strings[index_calc] in variables:
                    if len(operator) != 0 and unknown == False:
                        if operator == '+':
                            value += variables[strings[index_calc]]
                        elif operator == '-':
                            value -= variables[strings[index_calc]]
                        operator = ''
                    elif unknown == False:
                        value = variables[strings[index_calc]]

                elif strings[index_calc] not in variables and strings[index_calc] not in operators:
                    unknown = True
                    operator = ''
                    value = 0

                # Set operator
                if strings[index_calc] in operators and unknown == False:
                    operator = strings[index_calc]

                ans.append(str(strings[index_calc]))

            if unknown:
                print((" ").join(ans) + ' unknown')
            else:
                variable_name = variables_value.get(value)
                if variable_name:
                    print((" ").join(ans) + ' ' + variable_name)
                else:
                    print((" ").join(ans) + ' unknown')
                            
            ans = []