import sys
for line in sys.stdin:
    data = str(line)
    strings = data.replace("\n","").strip().split(' ')
    print(strings)