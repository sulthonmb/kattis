import sys

i = 1
text = ''
result = ''
for line in sys.stdin:
    data = str(line).strip().replace("\n", "")
    if (i == 1):
        text = data
    else:
        for j in range(int(data)):
            result = result + text
    i += 1

print(result)