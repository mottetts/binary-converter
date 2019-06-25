#Use to convert any positive base-10 integer into a binary number
#e.g. entering '22' returns '10110'
#Created in Python 3.6

def binary(n):
    exp = 0
    binlist = []
    while 2**exp <= n:
        if n % 2**(exp+1) == 0:
            binlist.insert(0,0)
        else:
            binlist.insert(0,1)
            n = n - 2**exp
        exp += 1
    return binlist

try:
    num = int(input('> '))
    outnum = binary(num)
    for i in outnum:
        print(i, end='')
except ValueError:
    print('Invalid input')