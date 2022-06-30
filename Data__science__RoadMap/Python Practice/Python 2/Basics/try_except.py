'''Exception in python'''
try:
    print('A DIV CAL')
    p = int(input('Enter a Dividend: '))
    q = int(input('Enter a Divisor: '))
    ans = p / q
    print("Ans is "+str(ans))
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
