"""
Дан массив букв, где каждая буква представляет фруктовое дерево.
Вам даны две корзины и ваша цель положить максимальное число фруктов в каждую
Лишь одно ограничение - каждая корзина может иметь только один тип фрукта.

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

"""


def fruits_into_baskets_one(tree):
    start = 0
    fuits_freq = {}
    max_length = 0

    for idx, fruit in enumerate(tree):
        fuits_freq[fruit] = fuits_freq.setdefault(fruit, 0) + 1
        while (len(fuits_freq) > 2):
            left_fruit = tree[start]
            fuits_freq[left_fruit] -= 1

            if fuits_freq[left_fruit] == 0:
                del fuits_freq[left_fruit]

            start += 1
        max_length = max(max_length, idx - start + 1)
    return max_length


def main():
    # assert fruits_into_baskets_one(['A', 'B', 'C', 'A', 'C']) == 3
    # assert fruits_into_baskets_one(['A', 'B', 'C', 'B', 'B', 'C']) == 5
    assert fruits_into_baskets_one([3,3,3,1,2,1,1,2,3,3,4]) == 5


main()
