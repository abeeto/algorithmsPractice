
def bestSum(target, nums, memo={}):
    if target in memo:
        return memo[target]
    elif target == 0:
        return []
    elif target < 0:
        return None

    for num in nums:
        remain = target - num
        tempNum = num
        # nums.remove(num)
        remainums = bestSum(remain, nums, memo)
        if remainums != None:
            memo[target] = tempNum
            remainums.append(memo[target])
            return remainums
    return None
#print(bestSum(7, [3,2]))
#print(bestSum(300, [7, 15]))
print(bestSum(7, [5, 3, 4, 1]))
#print(bestSum(8, [2,  3, 5]))
