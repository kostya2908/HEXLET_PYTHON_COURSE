'''
Операторы упаковки и распаковки — Python: Функции

    Оператор *
    Оператор **
    Выводы

В Python операторы * и ** используются, чтобы упаковывать и распаковывать итерабельные объекты и словари. Эти операторы обеспечивают гибкий способ обработки аргументов функций и позволяют писать функции, которые могут принимать переменное количество аргументов. В этом уроке мы узнаем, как пользоваться ими.
Оператор *

Оператор * используется для упаковки и распаковки итерируемых объектов, таких как списки или кортежи. При использовании перед итерируемым объектом, во время вызова функции, оператор * распаковывает его. Элементы итерируемого объекта передаются в качестве аргумента функции:

def sum_of_values(a, b, c):
    return a + b + c

values = [1, 2, 3]
result = sum_of_values(*values)
print(result)
# 6

В этом примере оператор * используется, чтобы распаковывать список значений и передавать его элементы в качестве аргументов функции sum_of_values.

Также оператор * можно использовать, чтобы упаковывать итерабельные переменные. Это позволяет присваивать их отдельным переменным:

my_list = [1, 2, 3, 4]
a, b, *c = my_list
print(a, b, c)
# 1 2 [3, 4]

В этом примере оператор * упаковывает оставшуюся часть списка my_list в переменную c.

Оператор * можно использовать для распаковки итерируемого списка в новый список или кортеж:

my_list = [1, 2, 3]
new_list = [*my_list, 4, 5, 6]
print(new_list)
# [1, 2, 3, 4, 5, 6]

my_tuple = (1, 2, 3)
new_tuple = (*my_tuple, 4, 5, 6)
print(new_tuple)
# (1, 2, 3, 4, 5, 6)

В этих примерах оператор * используется для распаковки итераций my_list и my_tuple в новые списки и кортежи с добавлением дополнительных значений.
Оператор **

Оператор ** используется для упаковки и распаковки словарей. При использовании перед словарем во время вызова функции оператор ** распаковывает пары ключ-значение словаря в аргументы ключевых слов, которые могут быть переданы в функцию:

def print_details(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

details = {"name": "John", "age": 30}
print_details(**details)
# Name: John
# Age: 30

В этом примере оператор ** используется для распаковки словаря details и передачи его пар ключ-значение в качестве аргументов ключевых слов в функцию print_details.

Оператор ** также можно использовать для создания словаря из последовательности пар ключ-значение:

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

combined_dict = {**dict1, **dict2}

print(combined_dict)
# {"a": 1, "b": 2, "c": 3, "d": 4}

В приведенном выше коде определяются два словаря dict1 и dict2. А оператор ** используется для распаковки их пар ключ-значение и объединения в один словарь combined_dict.

Если ключи дублируются, то значение из второго словаря перезапишет значение из первого словаря.
'''

'''
Напишите функцию get_unique(), которая принимает произвольное количество списков и возвращает список, содержащий все элементы из всех списков, но без повторений.

get_unique([1, 2, 3], [3, 4, 5], [5, 6, 7])  # [1, 2, 3, 4, 5, 6, 7]
'''

def get_unique(*args):
    S = set()    
    for _ in [*args]:
        S.update([*_])
    return list(S)







print(get_unique([1, 2, 3], [3, 4, 5], [5, 6, 7]))


