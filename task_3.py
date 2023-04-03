a = [9, 6, 45, 11, 0, 2, 9]
def sieve(lst):
    res = []
    for i in lst:
        if not (i in res):
            res = [i] + res
    return tuple(res)
print(sieve(a))