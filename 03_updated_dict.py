'''
Цель данного упражнения — функция updated(). Эта функция должна принимать словарь в качестве единственного позиционного аргумента (обязательного) и произвольное кол-во именованных аргументов. Возвращать же функция должна новый словарь, в котором ключи, соответствующие именованным аргументам, должны иметь сопутствующие значения (см.примеры).

d = {'a': 1, 'b': False}
updated(d, a=2, b=True, c=None)
# {'a': 2, 'b': True, 'c': None}
print(d)
# => {'a': 1, 'b': False}
updated(d) == d
# True
updated(d) is d
# False
'''
def updated(dicti, **kwargs):
    #print(dicti)
    #print(kwargs)
    result = dicti.copy()
    if kwargs:
        result.update(kwargs)
    return result




d = {'a': 1, 'b': False}
print(updated(d, a=2, b=True, c=None))

print(updated(d))
print(updated(d) == d)

print(updated(d) is d)

