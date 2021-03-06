# Создать список, содержащий цены на товары (10–20 товаров), например:
#
# [57.8, 46.51, 97, ...]
# * Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
#
prices = [57.8, 46.51, 97, 25.1, 77, 125.2, 16.27, 89, 11.11, 25.25]
prices.sort()


list = []
for i in range(len(prices)):
    item = f'{prices[i]:.2f}'
    item = item.split('.')
    item.insert(1, 'руб')
    item.append('коп')
    new_prices = ' '.join(item)
    list.append(new_prices)

print(list)

# * Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после
# сортировки остался тот же).
# * Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# * Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

