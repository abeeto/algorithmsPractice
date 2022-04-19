def gridTraverse(m,n,ways = {}):
    key = f"{m},{n}"
    if key in ways:
        return ways[key]
    if m == 0 or n == 0:
        return None
    if m == 1 or n == 1:
        return 1
    ways[key] = gridTraverse(m-1,n, ways) + gridTraverse(m, n-1, ways)
    return ways[key]
print(gridTraverse(18,18))