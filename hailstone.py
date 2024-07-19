import sys

def hailstone(number):
    result = int(number)

    if number == 1:
        return 1
    elif number % 2 == 0:
        return result + hailstone(number/2)
    else:
        return result + hailstone(3 * number + 1)

for line in sys.stdin:
    data = int(line)

    print(hailstone(data))

