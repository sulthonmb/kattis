import sys

for line in sys.stdin:
    data = str(line).strip().replace("\n", "").split(".")
    if len(data) == 1:
        print(data[0])
        break
    else:
        if int(list(data[1])[0]) >= 5:
            print(str(int(data[0]) + 1))
            break
        else:
            print(data[0])
            break
