def fibbonacci(n,memo = {}):
    start = {0: 0, 1: 1}
    if n in memo:
        return memo[n]
    if n == 0 or n==1:
        return start[n]
    
    memo[n] = fibbonacci(n-1, memo) + fibbonacci(n-2, memo)
    return memo[n]

#print(fibbonacci(100))


#wanted to see how a dynamic programming question would work with a ternary tree instead of a binary tree
#i.e  starting values = 0,1,2
# sequence: 0,1,2,3,6,11,20,37,68,125

def tripponacci(n, memo = {}):
    start = {1: 0, 2: 1, 3: 2}
    if n in memo:
        return memo[n]
    if n < 4:
        return start[n]
    
    memo[n] = tripponacci(n-3, memo) + tripponacci(n-2, memo) + tripponacci(n-1, memo)
    return memo[n]

print(tripponacci(10))