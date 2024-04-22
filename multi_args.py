def greet(x, *args):
    new = (x,) + args #new tuple with all names (x + args)
    print(f'Hello, ' + ' and '.join(new) + '!')    




greet('bob', 'mary', 'cunt', 'ass')
#greet('bob')
#greet('bob', 'ann')
#greet()
