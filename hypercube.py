import sys

def hamming_distance(string1, string2):
	dist_counter = 0
	for n in range(len(string1)):
		if string1[n] != string2[n]:
			dist_counter += 1
	return dist_counter

for line in sys.stdin:
    data = str(line).replace("\n","").split(" ")

    count = hamming_distance(data[1], data[2])
    print(count + 1)