def isValidSubsequence(array,sequence):
    for item in sequence:
        if (item not in array):
            return False
        else:
            ind = array.index(item)
            for i in range(ind+1):
                array.pop(0)        
    
    return True

def isValidSubsequence2(array, sequence):
    seqInd = 0
    for value in array:
        if seqInd == len(sequence):
            break
        if sequence[seqInd] == value:
            seqInd += 1
    return seqInd == len(sequence)

array = [5,1,22,25,6,-1,8,10]
sequence = [5,1,25,22,6,-1,8,10]

print(isValidSubsequence(array,sequence)) # True
