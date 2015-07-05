# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime

def parse_date(raw_date): # day, month, year
    return datetime.datetime.strptime(raw_date, '%d %m %Y')

def calculate_fine(actual_return_date, expected_return_date):
    fine = 0
    if actual_return_date > expected_return_date:
        same_month = actual_return_date.month == expected_return_date.month
        same_year = actual_return_date.year == expected_return_date.year
        if same_month and same_year:
            fine = 15 * (actual_return_date - expected_return_date).days
        elif same_year:
            fine = 500 * (actual_return_date.month - expected_return_date.month)
        else: 
            fine = 10000
    return fine

actual_return_date = parse_date(raw_input())
expected_return_date = parse_date(raw_input())
# actual_return_date = parse_date('31 8 2004')
# expected_return_date = parse_date('20 1 2004')

print calculate_fine(actual_return_date, expected_return_date)
