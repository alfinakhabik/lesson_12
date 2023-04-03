k = (1, 2, 3, 4, 5, 6, 7, 8, 2, 9, 10, 2, 3, 4, 3)
n = 3
def slicer(tpl, random_n):
    if random_n not in tpl:
        return ()
    if tpl.count(random_n) == 1:
        return tpl[tpl.index(random_n):]
    return tpl[tpl.index(random_n):tpl.index(random_n, tpl.index(random_n) + 1) + 1]
print(slicer(k, n))