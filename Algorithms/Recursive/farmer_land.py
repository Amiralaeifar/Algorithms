'''
    you are given a farm land, help the farmer to divide the land to biggest equal square size pieces.

    x and y are the height and width of the original land
    
    HINT: remember Divide & Conquer
    
'''

def divide_farm_land(x, y):
    if y > x:
        x, y = y, x
        
    x = x % y
    
    if ( x != 0):
        return divide_farm_land(x, y)
    else:
        return y
    
    
print( divide_farm_land(45, 12) ) # --> outputs 3