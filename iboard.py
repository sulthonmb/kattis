import sys

# 1 0

# 11111
# 10101

# 00000
# 10101

for line in sys.stdin:
    data = str(line)
    strings = data.replace("\n", "")

    ascii_list = []
    binaries_arr = []
    binaries = ''
    count_1 = 0
    count_0 = 0

    even_1 = False
    even_0 = False

    for string in strings:
        for char in string:
            ascii_list.append(ord(char))

    for ascii_value in ascii_list:
        binaries = str(bin(ascii_value)[2:])

        if binaries.count('1') % 2 == 1:
            even_1 = not even_1
        else:
            even_0 = not even_0
    
    # print('even_1', even_1)
    # print('even_0', even_0)

    if even_1 or even_0:
        print('trapped')
    else:
        print('free')