# https://docs.python.org/3/library/itertools.html
# https://habr.com/ru/company/otus/blog/529356/

import itertools

if __name__ == '__main__':
    # count(start=0, step=1) - бесконечный счетчик начиная с start=0 с шагом step=1
    # next_odd = itertools.count(1, 2)      счетчик начиная с 1 с шагом 2
    # [next(next_odd) for _ in range(5)]
    # [1, 3, 5, 7, 9]
    next_odd = itertools.count(1, 2)
    odds = [next(next_odd) for _ in range(5)]
    print(odds)

    # cycle(iterable) - бесконечный цикл по элементам iterable. Создает копию после первого прохождения по элементам
    # [next(itertools.cycle([0, 1])) - так лучше не делать :)
    zero_one = itertools.cycle([0, 1])
    print(next(zero_one), next(zero_one), next(zero_one), next(zero_one))

    # repeat(object[, times]) - возвращет объект times раз, либо бесконечно
    # itertools.repeat('one', 3)
    # ['one', 'one', 'one'] == ['one'] * 3
    for x in itertools.repeat('one', 3):
        print(x)

    # все возможные перестановки длины r=2, ПОРЯДОК ВАЖЕН (возвращает кортежи)
    # itertools.permutations('ABC', 2):
    # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
    for x in itertools.permutations('ABC', 2):
        print(x)

    # все возможные комбинации длины r=2, ПОРЯДОК НЕ ВАЖЕН (возвращает кортежи)
    # itertools.combinations([1, 2, 3], 2)
    # [(1, 2), (1, 3), (2, 3)]
    for x in itertools.combinations([1, 2, 3], 2):
        print(x)

    # декартово произведение
    # itertools.product([0, 1, 2], [3, 4]) == [(0, 4), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4)]
    # itertools.product([0, 1], [0, 1], [0, 1]) == itertools.product([0, 1], repeat=3)
    # [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
    print(list(itertools.product([0, 1], repeat=3)))