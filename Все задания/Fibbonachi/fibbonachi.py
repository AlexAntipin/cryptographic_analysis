def fibbonachi(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    else:
        result = fibbonachi(n - 1, memo) + fibbonachi(n - 2, memo)
        memo[n] = result
        return result

print(fibbonachi(4))