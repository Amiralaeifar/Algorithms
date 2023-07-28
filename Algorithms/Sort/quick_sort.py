def quick_sort(arr):
    if len(arr) < 2:
        return arr     # --> base case
    else:
        pivot = arr[0]
        smaller_than_pivot = [i for i in arr[1:] if i <= pivot]
        bigger_than_pivot = [i for i in arr[1:] if i > pivot]
        
        return quick_sort(smaller_than_pivot) + [pivot] + quick_sort(bigger_than_pivot)   # --> Recursive case
    
    
print( quick_sort([5, 2, 8, 3, 7, 4, 22]) )