import sys

i = 1
for line in sys.stdin:
    if i == 1:
        i += 1
        continue
    data = int(str(line).replace("\n", ""))
    if data % 2 == 0:
        print(str(data) + " is even")
    else:
        print(str(data) + " is odd")
