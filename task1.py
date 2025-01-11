list_vocale = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
your_text = input('Введите ваш текст: ')
vocales = [i for i in your_text if i in list_vocale]
print('Список гласных букв: ', vocales)
print('Длина списка: ', len(vocales))