import sys

numbers = []

for line in sys.stdin:
    numbers = list(int(x) for x in line.replace("\n", "").split(" "))
    print(abs(numbers[0] - numbers[1]))