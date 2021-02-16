#  Дан список:
#
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Новый список не создавать! Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов


sentence = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
sentence[1] = '05'
sentence[8] = '+05'
sentence.insert(1, '"')
sentence.insert(3, '"')
sentence.insert(5, '"')
sentence.insert(7, '"')
sentence.insert(12, '"')
sentence.insert(14, '"')
print(sentence)

part1 = ''.join(sentence[1:4])
part2 = ''.join(sentence[5:8])
part3 = ''.join(sentence[12:15])


sentence.remove('05')
sentence.remove('+05')
sentence.remove('17')


while sentence.count('"') > 0:
    sentence.remove('"')

sentence.insert(1, part1)
sentence.insert(3, part2)
sentence.insert(8, part3)

new_sentence = ' '.join(sentence)
print(new_sentence)