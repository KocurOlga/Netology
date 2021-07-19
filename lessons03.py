
def count_letters(word, letter):
    num_let = 0
    for letters in word:
        if letters == letter:
            num_let += 1
            break
    return num_let


my_list = ['python', 'c++', 'c', 'scala', 'java', 'r', 'perl']

symb = input('Введите букву для поиска: ')

num = 0
for elemtnt in my_list:
    count = count_letters(elemtnt, symb)
    num += count

print(num)
