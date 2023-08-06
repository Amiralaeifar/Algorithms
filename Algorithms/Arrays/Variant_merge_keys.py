'''
    Assuming the keys take one of three values, reorder the array so that all objects with
    the same key appear together. The order of the subarrays is not important.

'''

def reorder_by_key(arr):
    # create a dictionary to store the index for each value in lst:
    d = {}
    
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]] = []
            d[arr[i]].append(i)
        else:
            d[arr[i]].append(i)
    
    result_arr = []
    for key, values in d.items():
        for value in values:
            result_arr.append(key)
            
    return d, result_arr


print( reorder_by_key([3, 1, 2, 1, 1, 3]) )