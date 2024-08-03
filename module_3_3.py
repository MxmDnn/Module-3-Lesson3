# 1. Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True) :
    print(a,b,c)

print_params()
print_params(4,3, 1)
list_=(4,3)
print_params(list_,)
print_params(*list_,1)
print_params(b=25)
print_params(c=[1,2,3])

# 2. РАспаковка параметров
value_list=('Winny the Pooh', 13, False)
value_dict=dict(a=True, b='Piglet', c=[2023,2025])
print_params(*value_list)
print_params(**value_dict)

# 3. Распаковка + отдельные параметры
value_list_2=(54.32, 'Строка')
print_params(*value_list_2,42)
