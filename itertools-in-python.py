import itertools

if __name__ == '__main__':
    # бесконечный счетчик начиная с start=10 с шагом step=2
    count = itertools.count(10, 2)
    print(next(count))
    print(next(count))
    print(next(count))
    # все возможные перестановки (в кортежах)
    for x in itertools.permutations([1, 2, 3]):
        print(x)

    # все возможные комбинации определенной длины (в кортежах)
    for x in itertools.combinations([1, 2, 3, 4], 2):
        print(x)
