def g(n):
    if n > 14 and n < 20:
        return n
    elif n <= 14 and n > 0:
        return g(4 * n)
    elif n <= 0:
        return g(-n + 1)
    else:
        return g(n - 10)
print(g(40))


# g(n) does not terminate when n is either 5 or a multiple of 10 
