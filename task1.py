import string

input_letters = input("Введіть дві букви через дефіс (наприклад, A-D): ")

all_letters = string.ascii_letters

start_index = all_letters.index(input_letters[0])

end_index = all_letters.index(input_letters[2])

extracted_characters = all_letters[start_index:end_index + 1]

print("Результат:", extracted_characters)