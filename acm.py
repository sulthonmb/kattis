import sys

for line in sys.stdin:
    data = str(line).replace("\n", "").split(" ")
    
    print(data)