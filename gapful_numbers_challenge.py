"""L.Colucci calls a number  n  of at least 3 digits a gapful number if  n  is divisible by
the number formed by the first and last digit of  n.
For example, 583 is gapful because it is divisible by 53.
This program checks if the entered number is gapful number."""

import sys

def div(num):
    res = ''
    res += num[0]
    res += num[-1]
    return int(res)

def checkGap(num):
    n = int(num)
    d = div(inp)
    if n%d == 0:
        return True
    return False




inp = input('Enter integer(3+ digits):\n')
lng = len(inp)
if lng<3:
    print('Entered number should have minimum 3 digits.')
    sys.exit()
if(checkGap(inp)):
    print('Number {} is Gapful Number.'.format(inp))
else:
    print('Number {}  is NOT a Gapful number.'.format(inp))
