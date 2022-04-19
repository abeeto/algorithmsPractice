class fibonacci:
    #memoization    
    nums = [0,1]
    @classmethod 
    def fib(self, n):
        if n < len(self.nums):
            return self.nums[n-1]
        else:
            tempNum = self.fib(n-2) + self.fib(n-1)
            self.nums.append(tempNum)
            return tempNum


print(fibonacci.fib(10))
        