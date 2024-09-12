def twoNumberSum(array, targetSum):
    array.sort()
    for i in range(len(array)-1):
        for j in range(len(array)-1,i,-1):
            print(array[i],array[j])
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
            else:
                if array[i] + array[j] < targetSum:
                    break
    return []

def twoNumberSum2(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
        


array = [3,5,-4,8,11,1,-1,6]
targetSum = 10

array = [4,6]
targetSum = 10

print(twoNumberSum(array, targetSum)) # [11, -1] or [-1, 11]
