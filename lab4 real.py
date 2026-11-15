
from itertools import combinations
from pathlib import Path

items = {
    'r': (3, 25), 'p': (2, 15), 'a': (2, 15),
    'm': (2, 20), 'i': (1, 5), 'k': (1, 15),
    'x': (3, 20), 't': (1, 25), 'f': (1, 15),
    'd': (1, 10), 's': (2, 20), 'c': (2, 20)
}


def solve(capacity):
    total = 0
    for size, value in items.values():
        total += value

    best_score = -1000
    best_items = []
    valid = []

    for n in range(len(items) + 1):
        for choice in combinations(items, n):
            size = 0
            value = 0
            for name in choice:
                size += items[name][0]
                value += items[name][1]

            score = 15 + value - (total - value)

            if size <= capacity:
                if score > best_score:
                    best_score = score
                    best_items = choice
                if score > 0:
                    valid.append((choice, score))

    print('Вместимость:', capacity)
    print('Лучшие предметы:', best_items)
    print('Итоговые очки выживания:', best_score)
    print('Положительных комбинаций:', len(valid))

    if capacity == 9:
        cells = []
        for name in best_items:
            cells += [name] * items[name][0]

        for i in range(0, len(cells), 3):
            print(' '.join('[' + x + ']' for x in cells[i:i + 3]))

        with open(Path(__file__).parent / 'all_combinations.txt',
                  'w', encoding='utf-8') as file:
            for choice, score in valid:
                file.write(f'{" ".join(choice)} : {score}\n')


solve(9)
print()
solve(7)
