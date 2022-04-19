from inspect import stack


def uniqueSum(target, numbers):
    if target == 0:
        return []
    if target < 0:
        return None
    
    for index in range(len(numbers)):
        remain = target - numbers[index]
        newStart = index + 1
        remainums = uniqueSum(remain, numbers[newStart:len(numbers)])
        #staynums = bestSum(target, numbers[newStart:len(numbers)])
        if remainums != None:
            remainums.append(numbers[index])
            return remainums
print(uniqueSum(6, [2,3,4]))