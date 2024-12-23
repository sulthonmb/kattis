import sys

skip = 0
count_list_phone_number = 0
count_phone_number = 0
list_phone_numbers = []
set_phone_numbers = []

for line in sys.stdin:
    data = str(line.replace('\n', ''))
    if skip == 0:
        count_list_phone_number = data
        skip += 1
        continue
    
    if count_phone_number == 0:
        count_phone_number = int(data)
        continue
    
    count_phone_number -= 1
    set_phone_numbers.append(data)

    if count_phone_number == 0:
        if len(set_phone_numbers) != 0:
            set_phone_numbers = sorted(set_phone_numbers, key=lambda x: (x != "0", int(x)))
            list_phone_numbers.append(set_phone_numbers)
            set_phone_numbers = []
    
for list_phone_number in list_phone_numbers:
    prefix_phone_number = set()
    found_not_consistent = False

    for phone_number in list_phone_number:
        if len(prefix_phone_number) == 0:
            prefix_phone_number.add(phone_number)
            continue

        digits_call = list(phone_number)
        recipient_phone_number = ''
        for digit_call in digits_call:
            recipient_phone_number += digit_call
            if recipient_phone_number in prefix_phone_number:
                found_not_consistent = True
                break
        
        if found_not_consistent:
            break
        else:
            prefix_phone_number.add(phone_number)
        

    if found_not_consistent:
        print('NO')
    else:
        print('YES')

