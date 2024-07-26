import sys

for line in sys.stdin:
    data = str(line.strip())
    first_price = 1000
    first_year = 2020

    year_now = data

    if int(year_now) <= int(first_year):
        print(first_price)
        break

    distance_year = int(year_now) - int(first_year)

    final_price = first_price + (100*distance_year)

    print(final_price)