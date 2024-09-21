# 1 задание
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b = 25)
print_params(c = [1, 2, 3])
print_params()
print_params(1, 4)

# 2 задание
values_list = [1, 2, 3]
values_dict = {'a': 'sigma', 'b': 23, 'c': False}
print_params(*values_list)
print_params(**values_dict)

# 3 задание
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

