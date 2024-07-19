import sys
from collections import deque

i = 0
bit = ''
# Convert Z to 0 and O to 1 it will be binary and convert binary to decimal
for line in sys.stdin:

    if i == 0:
        i += 1
        continue

    data = str(line).replace("\n", "")

    if data == 'O':
        bit += '1'
    else:
        bit += '0'

bits = deque(list(bit))
bits.reverse()

ans = 0
binary = 1
for bit_val in bits:
    if bit_val == '1':
        if i == 1:
            ans = 1
            i += 1
            binary *= 2
        else:
            ans += binary
            binary *= 2
            i += 1
    else:
        binary *= 2
        i += 1

print(ans)
