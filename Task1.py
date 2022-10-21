"""
Напишите функцию change(lst),
которая принимает список и меняет местами его первый и последний элемент.
В исходном списке минимум 2 элемента.
"""


def change(lst):
    i = lst.pop()  # Удаляем последний элемент и сохраняем его в переменную
    j = lst.pop(0)  # Удаляем первый элемент и сохраняем его в переменную
    lst.insert(0, i)  # Добавляем к списку новый первый элемент
    lst.append(j)  # Добавляем к списку новый последний элемент
    return lst


print(change([1, 2, 3, 4, 5, 6, 7]))