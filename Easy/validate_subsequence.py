def isValidSubsequence(array,sequence):
    for item in sequence:
        if (item not in array):
            return False
        else:
            ind = array.index(item)
            for i in range(ind+1):
                array.pop(0)        
    
    return True

array = [5,1,22,25,6,-1,8,10]
sequence = [5,1,25,22,6,-1,8,10]

print(isValidSubsequence(array,sequence)) # True
