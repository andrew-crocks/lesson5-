import random

num_elements = random.randint(3, 10)

input_numbers = input(f"Введіть {num_elements} числа розділені пробілами: ")

random_list = [int(num) for num in input_numbers.split()]

print("Початковий список:", random_list)

if len(random_list) >= 3:

    new_list = [random_list[0], random_list[2], random_list[-2]]
    print("Новий список:", new_list)
else:
    print("Список має недостатньо елементів. Введіть щонайменше 3 числа")

