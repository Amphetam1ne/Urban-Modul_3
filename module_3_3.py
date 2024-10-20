def print_params(a=1, b='строка', c=True):
    '''Задача "Распаковка"'''
    print(a, b, c)


print_params()
print_params(b=33)  # функция print_params с разным количеством аргументов, включая вызов без аргументов
print_params(a='urbam', c=False)

values_list = [77, 'apple', False]
values_dict = {'a': 66, 'b': 'jobs', 'c': None}

print_params(*values_list)  # Распаковка списка
print_params(**values_dict)  # Распааковка словаря

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # Распаковка списка
