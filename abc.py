import sys

i = 0
numbers = []
orders = []
values = {}
chr_first = ord('A')
res = []

for line in sys.stdin:
    if (i == 0):
        numbers = list(int(x) for x in line.replace("\n","").split(" "))
        i += 1
    else:
        orders = list(str(line.replace("\n","")))

numbers.sort()

for number in numbers:
    if values == {}:
        values[chr(chr_first)] = number
    else:
        chr_first += 1
        values[chr(chr_first)] = number

for order in orders:
    res.append(str(values[order]))

print(' '.join(res))
