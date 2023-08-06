'''
    write a program which takes as input an arrau of digits encoding a nonnegative decimal
    integer D and updated the array to represent the integer D+1
    
    input --> [1, 2, 9]  output --> [1, 3, 0]
'''

def increment_precision(arr):
    #finding the number represented in the arr
    number = arr[0] * 10 + arr[1]
    
    i = 2
    while i < len(arr):
        number = number * 10 + arr[i]
        i += 1
        
    number += 1 #increment number by one
    
    result_arr = []
    while number > 0:
        digit = number % 10
        result_arr.append(digit)
        number = number // 10
        
    return list(reversed(result_arr))


print( increment_precision([9, 9, 9]) )