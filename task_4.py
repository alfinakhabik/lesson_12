a = (1, 9, 9, 6, 8, 17, 2, 9)
n = 6
def del_from_tuple(tpl, number):
    if not (number in tpl):
       return tpl
    else:
        k = tpl.index(number)
        return tuple(list(tpl)[0:k] + list(tpl[k + 1:]))

print(del_from_tuple(a, n))