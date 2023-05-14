# Дана строка ( возможно, пустая), состоящая
# из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
# BBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе
# даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла
# невалидная строка.Пояснения:
# Если символ встречается 1 раз, он остается
# без изменений; Если символ повторяется более
# 1 раза, к нему добавляется количество повторений.

def rle(string):
    total = ""
    i = 0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count += 1
            i += 1
        if count == 1:
            total += string[i]
        else:
            total += string[i] + str(count)
        i += 1
    return total

line = str(input("введите строку букв:   "))
valid = set('QWERTYUIOPASDFGHJKLZCXVBNM')
if (set(line).issubset(valid)):
    print(rle(line))
else:
    print('невалидная строка')