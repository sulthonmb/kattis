import sys

circuits = {}
combinations = []
i = 0
result = []

def circuit_to_boolean(circuit):
    if circuit == 'T':
        return True
    else:
        return False

def boolean_to_circuit(circuit):
    if circuit == True:
        return 'T'
    else:
        return 'F'

for line in sys.stdin:
    data = str(line)

    if i == 0:
        i += 1
        continue
    elif i == 1:
        strings = data.replace("\n","").split(" ")
        for j in range(len(strings)):
            x = 'A'
            circuits[chr(ord(x) + j)] = strings[j]

        i += 1
        continue
    elif i == 2:
        strings = data.replace("\n","").split(" ")
        for j in range(len(strings)):
            combinations.append(strings[j])

try:
    for combination in combinations:
        if combination not in {'*', '+', '-'}:
            result.append(circuits[combination])
        elif combination == '*':
            first_circuit = circuit_to_boolean(result.pop())
            second_circuit = circuit_to_boolean(result.pop())

            result.append(boolean_to_circuit(first_circuit and second_circuit))
        elif combination == '+':
            first_circuit = circuit_to_boolean(result.pop())
            second_circuit = circuit_to_boolean(result.pop())

            result.append(boolean_to_circuit(first_circuit or second_circuit))
        elif combination == '-':
            first_circuit = circuit_to_boolean(result.pop())
            result.append(boolean_to_circuit(not first_circuit))

    if len(result) == 0:
        print('F')
    else:
        print(result[0])
except:
    print('F')

