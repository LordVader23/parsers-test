import re

# if re.compile('^[A-Z]{3,5}$').findall('AB'.strip()):
#     print('yes')
#
# for (index, (a, b)) in enumerate(zip(list(range(5)), list(range(5)))):
#     print(index, a, b)

f = open(r'proxies.txt', 'r')

for i in f:
    # a = i.strip()
    i = i.replace('\t', ' ')
    i = i.replace('\n', '')
    a = i.split(' ')
    print(a)

a = '<div class="inner-entry__details">\n\t\t\t<strong>Год выпуска: </strong> 28 февраля 2017 для PlayStation 4 / 07 августа 2020 для PC<br>\n\t\t\t<strong>Жанр: </strong> <a href="https://v.otxataba.net/torrent_igry/rpg/">RPG</a> / <a href="https://v.otxataba.net/torrent_igry/action/">Action</a> / <a href="https://v.otxataba.net/torrent_igry/adventure/">Adventure</a> / <a href="https://v.otxataba.net/torrent_igry/licenzii/">Лицензии</a> / <a href="https://v.otxataba.net/torrent_igry/2017/">2017 года</a> / <a href="https://v.otxataba.net/torrent_igry/2020/">2020 года</a><br>\n\t\t\t<strong>Разработчик: </strong> Guerrilla<br>\n\t\t\t<strong>Издатель:</strong>  PlayStation Mobile<br>\n\t\t\t<strong>Тип издания:</strong>  Сценовый релиз от CODEX<br>\n\t\t\t<strong>Язык интерфейса: </strong> Русский, Английский, MULTi20<br>\n\t\t\t<strong>Язык озвучки: </strong> Русский, Английский, MULTi11<br>\n\t\t\t<strong>Таблэтка: </strong> CODEX <br>\n    </div>'
a = 'Разработчик: </strong> Paradox Development Studio<br>'
# b = re.search(r'Разработчик: </strong> ([A-Z]{1}[a-z]+)<br>', a).group(1)
b = re.search(r'Разработчик: </strong> (\w+)<br>', a).group(1)
print(b)

arr = [1, 2, 3, 3, 3, 2, 2]
c = set(arr)
c = list(c)
print(c)
