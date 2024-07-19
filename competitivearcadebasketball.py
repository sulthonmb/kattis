#! /usr/bin/python2
import sys

participants = {}
total_participants = 0
minimum_point_to_win = 0
start_score = 0
winners = []

i = 0
for line in sys.stdin:
    data = str(line)

    if i == 0:
        base_data = data.replace("\n", "").split(' ')
        total_participants = int(base_data[0])
        minimum_point_to_win = int(base_data[1])
        start_score = int(base_data[2])
        i += 1
    elif i > 0:
        data = data.replace("\n", "").split(' ')
        for j in range(len(data)):
            if len(data) == 1:
                participants[data[j]] = 0
            else:
                participants[data[j]] += int(data[j+1])
                break

no_winner = True

for i in participants:
    if int(participants[i]) >= minimum_point_to_win:
        winners.append(i)
        no_winner = False

if no_winner:
    print("No winner!")
else:
    for winner in winners:
        print(winner + " wins!")
