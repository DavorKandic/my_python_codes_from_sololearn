import sys

months = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
print('Please enter today\'s date in dd-mm-yyyy format:')
date = input()
print('Enter number of days from today:')
days = int(input())
date_lst = date.split('-')
date_lst = [int(num) for num in date_lst]
dd, mm, yyyy = date_lst[0], date_lst[1], date_lst [2]
if days > months[mm]:
    print('Sorry, number is too big.')
    sys.exit()
ind = mm - 1
sum_of_days = dd + days
if sum_of_days <= months[ind]:
    dd = sum_of_days
    print(f'New date is: {dd}-{mm}-{yyyy}')
else:
    dd = sum_of_days - months[ind]
    if mm == 12:
        mm = 1
        yyyy += 1
    else:
        mm += 1
    print(f'New date is: {dd}-{mm}-{yyyy}')
    
