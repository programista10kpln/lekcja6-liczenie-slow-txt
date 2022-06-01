import string


def count_words(name):
    with open(name, 'r', encoding='utf-8') as file:
        if file.readable():
            words = file.read()
        else:
            return 'błąd'
        number_words = len(words)

        alphabet_string = string.ascii_lowercase
        alphabet_list = list(alphabet_string)
        result = {}

        for i in alphabet_list:
            counted_words = words.lower().count(i)
            percentage = (counted_words / number_words) * 100
            result[i] = str(counted_words) + ' - ' + str(round(percentage, 2)) + ' %'

    with open('wynik.txt', 'w', encoding='utf-8') as result_file:
        if result_file.writable():
            result_file.write('Ilość wszystkich liter: ' + str(number_words) + '\n')
            for key, value in result.items():
                result_file.write(key.upper() + ' - ' + value + '\n')
        else:
            return 'błąd'


count_words('tekst.txt')
