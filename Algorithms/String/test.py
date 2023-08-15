from functools import reduce
import string

def str_to_int(s):
    return reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)


def int_to_str(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
        
    result = []
    while True:
        result.append(chr(ord('0')+ x % 10))
        x = x // 10
        if x == 0:
            break

    return result 


print(int_to_str(123))
print(str_to_int('123'), type(str_to_int('123')))