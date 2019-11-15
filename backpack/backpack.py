# %%
from collections import Counter


def backpack(items: list, backpack_capacity: int, auto_fill: bool = False) -> dict:
    """
    Функция для решения задачи о рюкзаке
    :param items: список предметов [(вес, стоимость), ...]
    :param backpack_capacity: вместимость рюкзака
    :param auto_fill: разрешение использовать один предмет несколько раз
    :return: словарь с ключами:
        :cost: int - итоговая стоимость
        :weights: list - веса предметов, которые будут добавлены в рюкзак
        :weights_plus: list - [(вес_предмета, количество_его_добавлений_в_рюкзак), ...]
    """

    if auto_fill:
        for item in items[:]:
            items.extend([item] * (backpack_capacity // item[0] - 1))

    weights = tuple(range(backpack_capacity + 1))
    items = ['0'] + items

    table = [[0] * len(weights) for _ in range(len(items))]
    weights_table = [[list()] * len(weights) for _ in range(len(items))]

    for i in range(1, len(items)):
        for w in range(1, len(weights)):
            if items[i][0] <= w:
                if table[i - 1][w] > table[i - 1][w - items[i][0]] + items[i][1]:
                    table[i][w] = table[i - 1][w]
                    weights_table[i][w] = weights_table[i - 1][w]
                else:
                    table[i][w] = items[i][1] + table[i - 1][w - items[i][0]]
                    weights_table[i][w] = [items[i][0]] + weights_table[i - 1][w - items[i][0]]
            else:
                table[i][w] = table[i - 1][w]
                weights_table[i][w] = weights_table[i - 1][w]

    cost = table[-1][-1]
    weights = weights_table[-1][-1]
    weights_plus = Counter(weights).most_common()

    return {'cost': cost, 'weights': weights, 'weights_plus': weights_plus}


# example
data = [
    (2, 3),
    (3, 4),
    (5, 6)
]

print(backpack(data, 10, False))
print(backpack(data, 10, True))
