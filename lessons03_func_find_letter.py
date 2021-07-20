
def count_letters(word_list, letter):
    '''Функция ищет букву в каждом слове списка. Если буква найдена, счетчик плюсует 1:
    :param: word_list - список, в котором ищем букву
    :param: letter - буква, которую ищем'''
    num_let = 0
    for word in word_list:
        if letter in word:
            num_let += 1
    return num_let


print(count_letters(['python', 'c++', 'c', 'scala', 'java', 'r', 'perl'], 'c'))
