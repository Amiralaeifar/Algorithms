'''
    a palindromic string is one which reads the same when it is reversed.
'''

# O(n) Time and O(1) Space Complexity.
def is_palindromic(string):
    # NOTE: s[~i] for i in [0, len(s) - 1] is s[-(i + 1)]
    return all(string[i] == string[~i] for i in range(len(string) // 2))


print( is_palindromic('garag') )