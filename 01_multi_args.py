'''
Вам нужно реализовать функцию greet(), которая должна принимать несколько имён (как минимум одно!) и возвращать строку приветствия (см. примеры ниже).

greet('Bob')
# 'Hello, Bob!'
greet('Moe', 'Mary')
# 'Hello, Moe and Mary!'
greet(*'ABC')
# 'Hello, A and B and C!'

'''

def greet(x, *args):
    new = (x,) + args #new tuple with all names (x + args)
    print(f'Hello, ' + ' and '.join(new) + '!')    




greet('bob', 'mary', 'cunt', 'ass')
#greet('bob')
#greet('bob', 'ann')
#greet()
