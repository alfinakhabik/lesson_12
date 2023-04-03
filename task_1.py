k = (-111, 99, 15, 7, 5.5)
def tpl_sort(tpl):
    for i in tpl:
        if int(i) == i:
            return tuple(sorted(tpl))
        else:
            return tpl
print(tpl_sort(k))