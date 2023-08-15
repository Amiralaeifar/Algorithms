import string
import functools

def construct_to_base(num, base):
    return ( '' if num == 0 else
            construct_to_base(num // base, base) + 
            string.hexdigits[num % base].upper())
    
def construct_to_base10(num):
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        num, 0
    )

print( construct_to_base(615, 13) )
print( construct_to_base10())