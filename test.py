import sys
for line in sys.stdin:
    left = False
    right = False
    count_1 = 0
    count_0 = 0
    for char in line.strip():
        binary = str(format(ord(char), 'b'))
        count_1 += binary.count('1')
        count_0 += binary.count('0')
        # print("binary.count('1')", str(binary.count('1')))
        # print("binary.count('0')", str(binary.count('0')))
        
        if binary.count('1') % 2 == 1:
            left = not left
        else:
            right = not right
    
    print('count_1', count_1 % 2, 'left', left)
    print('count_0', count_0 % 2, 'right', right)
    print("trapped" if left or right else "free")