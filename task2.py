number = int(input("Введіть ціле число більше нуля: "))

if number <= 0:
    print("Введене число не задовольняє умову.")
else:
    product = 1

    while number > 0:
        digit = number % 10
        product *= digit
        number //= 10

    while product > 9:
        result = 1
        while product > 0:
            digit = product % 10
            result *= digit
            product //= 10
        product = result

    print("Добуток цифр числа:", product)