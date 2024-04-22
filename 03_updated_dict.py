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

