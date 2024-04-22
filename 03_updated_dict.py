'''
Больше об именованных аргументах — Python: Функции

    Получение именованных аргументов в виде словаря
    Порядок вызовов смешанных аргументов
    Передача именованных аргументов с помощью словаря
    Keyword-only аргументы
    Порядок аргументов при вызове функций
    Выводы

В этом уроке мы разберем, как получать произвольное количество именованных аргументов, как передавать их в виде коллекции и как объявлять keyword-only аргументы.
Получение именованных аргументов в виде словаря

Позиционные аргументы можно получать в виде *args, причем в произвольном количестве. Для именованных аргументов тоже существует подобная возможность. Только они получаются в виде словаря, что позволяет сохранить имена аргументов в ключах:

def g(**kwargs):
    return kwargs

g(x=1, y=2, z=None)
# {'x': 1, 'y': 2, 'z': None}

По соглашению аргумент, который получает подобный словарь, принято называть kwargs — от словосочетания keyword arguments.
Порядок вызовов смешанных аргументов

Поэкспериментируем с разными комбинациями аргументов, которые можно передавать функциям:

def f(*args, **kwargs):
    return (args, kwargs)

f(1, 2, 3, 4, kx='a', ky='b', kz='c')
# ((1, 2, 3, 4), {'kx': 'a', 'ky': 'b', 'kz': 'c'})

Заметим, что *args всегда указывается перед **kwargs, иначе будет ошибка:

def f(**kwargs, *args):
    return (kwargs, args)

f(1, kx='a') # SyntaxError: invalid syntax

Также при объявлении функций можно комбинировать позиционные аргументы, значения по умолчанию, *args и **kwargs одновременно. При использовании обычных позиционных аргументов их следует добавлять в начало перед аргументом *args:

def f(x, *args, **kwargs):
    return (x, args, kwargs)

f(1, 2, 3, kx='a', ky='b')
# (1, (2, 3), {'kx': 'a', 'ky': 'b'})

Аргументы со значением по умолчанию следует добавлять после аргумента *args, но перед аргументом **kwargs:

def f(*args, ky=42, **kwargs):
    return (args, ky, kwargs)

f(1, 2, 3, 4, kz='c')
# ((1, 2, 3, 4), 42, {'kz': 'c'})

f(1, 2, 3, 4, ky='b', kz='c')
# ((1, 2, 3, 4), 'b', {'kz': 'c'})

Аргумент *args в определении функции пишется после всех обычных позиционных аргументов, но перед первым аргументом со значением по умолчанию. А **kwargs пишется в самом конце после последнего аргумента со значением по умолчанию.

Согласно этому правилу у нас идет следующий порядок расстановки аргументов:

    Обычные позиционные аргументы
    Аргумент *args
    Аргументы со значением по умолчанию
    Аргумент **kwargs

def f(x, y, *args, kx=None, ky=42, **kwargs):
    return (x, y, args, kx, ky, kwargs)

f(1, 2, 3, 4, kx='a', ky='b', kz='c')
# (1, 2, (3, 4), 'a', 'b', {'kz': 'c'})

В реальном коде редко какая функция использует все эти возможности одновременно. Но понимать, как работает каждая форма объявления аргументов, и как такие формы можно сочетать, — очень важно.
Передача именованных аргументов с помощью словаря

Как и в случае позиционных аргументов, именованные можно передавать в функцию пачкой в виде словаря. Для этого перед словарем нужно поставить две звездочки. Пример:

def coords(x, y):
    return (x, y)

coords(x=1, **{'y': 2})
# (1, 2)

Здесь указан обычный именованный аргумент, а другой завернут в словарь.

Попробуем вызвать функцию с двумя наборами аргументов: для позиционных и для именованных:

def f(x, y, *args, kx=None, ky=42, **kwargs):
    return (x, y, args, kx, ky, kwargs)

positional = (2, 3)
named = dict(ky='b', kz='c')
f(1, *positional, 4, kx='a', **named)
# (1, 2, (3, 4), 'a', 'b', {'kz': 'c'})

В этом примере мы не написали литерал, а вместо этого вызвали функцию dict с несколькими именованными аргументами. Так словарь еще больше похож на сохраненный набор аргументов.

При подстановке аргументов разворачивающиеся наборы аргументов вроде *positional и **named можно указывать вперемешку с аргументами соответствующего типа: *positional — с позиционными, **named — с именованными. При этом все именованные аргументы должны идти после всех позиционных.
Keyword-only аргументы

В Python 3 добавили возможность пометить именованные аргументы функции так, чтобы вызывать функцию можно было только через передачу этих аргументов по именам. Такие аргументы называются keyword-only и их нельзя передать в функцию в виде позиционных. Выглядит функция с подобными аргументами так:

def open_file(name, *, writable=False, binary=False):
    …

f1 = open_file('foo.txt', writable=True)
f2 = open_file('bar.bin', binary=True)
f3 = open_file('raw.dat', True, True)
# TypeError: open_file() takes 1 positional argument but 3 were given

Здесь * выступает разделителем — отделяет обычные аргументы от строго именованных. Такой разделитель можно использовать только один раз в одном определении. Еще его нельзя применять в функциях с *args. Но можно объявлять функции, у которых будут только строго именованные аргументы. Для этого нужно поставить звездочку в самом начале перечня аргументов.

Этот пример демонстрирует подход к описанию аргументов. Первый аргумент — имя файла, который будет открыт. Оно всегда присутствует и связано по смыслу с именем функции. Поэтому этот аргумент можно не именовать. А writable и binary — необязательные аргументы, которые получают значения True/False. Поэтому опции и объявлены так, что могут быть указаны только явно.

Когда мы используем keyword-only аргументы вместе с именованными аргументами (**kwargs), возникает проблема. Именованные аргументы могут перехватить значения, которые должны были быть переданы как keyword-only аргументы. В итоге это может привести к ошибкам в работе функции.

Рассмотрим следующий пример:

def my_func(a, *, b=None, **kwargs):
    print(a, b, kwargs)

my_func(1, b=2, c=3)
# 1 2 {'c': 3}

В данном примере аргумент a принимает значение 1, а keyword-only аргумент b — значение 2. При этом аргумент c передается в **kwargs, что может привести к ошибке, если c не должен был передаваться этой функции.

Поэтому рекомендуется использовать либо keyword-only аргументы, либо **kwargs, но не оба вместе. Это поможет избежать неожиданного поведения и ошибок в работе функции.
Порядок аргументов при вызове функций

При вызове функций у нас больше свободы, чтобы задать порядок аргументов. Одиночные именованные аргументы могут идти вперемешку с подстановками наборов позиционных. Вот пример такого вызова:

def f(x, y, *args, kx=None, ky=42, **kwargs):
    return (x, y, args, kx, ky, kwargs)

foo = [1, 2, 3]
bar = "abc"
f(kx=42, *foo, ky=100, *bar)
# (1, 2, (3, 'a', 'b', 'c'), 42, 100, {})

Еще одна особенность заключается в том, что мы не можем одновременно указать аргумент x по имени и при этом развернуть набор параметров для функции с сигнатурой вида f(x, *args). То есть мы не сможем сделать так: f(*foo, x=42).
Выводы

В этом уроке мы изучили несколько важных концепций, которые позволяют управлять аргументами функций в Python. Мы рассмотрели способ получения именованных аргументов в виде словаря, порядок вызовов смешанных аргументов, способ передачи именованных аргументов с помощью словаря и работу с keyword-only аргументами.

Важно помнить, что порядок передачи аргументов должен соответствовать порядку, который задан при объявлении функции. Если мы нарушаем порядок, мы можем получить ошибку.
'''

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

