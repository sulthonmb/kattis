import sys

i = 1
count_bags = 0
num_bag = 0
for line in sys.stdin:
    data = str(line).strip().replace("\n", "").split(" ")

    if i == 1:
        count_bags = int(data[0])
        num_bag = int(data[1])
    else:
        for j in range(len(data)):
            if int(data[j]) == num_bag and j == 0:
                print('fyrst')
                break
            elif int(data[j]) == num_bag and j == 1:
                print('naestfyrst')
                break
            elif int(data[j]) == num_bag:
                print( str(j+1) + ' fyrst')

    i += 1
