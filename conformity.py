#! /usr/bin/python3
import sys

numbers = []
strings = {}
most_popular = 0
ans = 0

for line in sys.stdin:
    data = str(line)
    num_string = data.split(' ')
    if (len(num_string) > 1):
        num_int = [int(val) for val in num_string]
        num_int.sort()

        num__string_sort = ' '.join(map(str, num_int))
        if num__string_sort in strings:
            strings[num__string_sort] += 1
        else:
            strings[num__string_sort] = 1

for key in strings:
    if strings[key] > most_popular:
        most_popular = strings[key]
        ans = strings[key]
    elif strings[key] == most_popular:
        ans += strings[key]

print(ans)