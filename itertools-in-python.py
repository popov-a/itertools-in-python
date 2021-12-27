# https://docs.python.org/3/library/itertools.html
# https://habr.com/ru/company/otus/blog/529356/

import itertools

if __name__ == '__main__':
    # count(start=0, step=1) - бесконечный счетчик начиная с start=0 с шагом step=1
    next_odd = itertools.count(1, 2)    # счетчик начиная с 1 с шагом 2
    odds = [next(next_odd) for _ in range(5)]
    print(odds)

    # cycle(iterable) - бесконечный цикл по элементам iterable. Создает копию после первого прохождения по элементам
    zero_one = itertools.cycle([0, 1])
    print(next(zero_one), next(zero_one), next(zero_one), next(zero_one))

    # repeat(object[, times]) - возвращет объект times раз, либо бесконечно
    for x in itertools.repeat('one', 3):
        print(x)

    # все возможные перестановки длины r=2, порядок важен (возвращает кортежи)
    for x in itertools.permutations('ABC', 2):
        print(x)

    # все возможные комбинации длины r=2, порядок не важен (возвращает кортежи)
    for x in itertools.combinations([1, 2, 3], 2):
        print(x)
