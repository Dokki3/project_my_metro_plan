data = {
    # line 1
    ('Бульвар Рокоссовского', 'Черкизовская'): 3,
    ('Черкизовская', 'Преображенская площадь'): 3,
    ('Преображенская площадь', 'Сокольники'): 4,
    ('Сокольники', 'Красносельская'): 2,
    ('Красносельская', 'Комсомольская1'): 2,
    ('Комсомольская1', 'Красные Ворота'): 2,
    ('Красные Ворота', 'Чистые пруды'): 2,
    ('Чистые пруды', 'Лубянка'): 2,
    ('Лубянка', 'Охотный Ряд'): 2,
    ('Охотный Ряд', 'Библиотека имени Ленина'): 2,
    ('Библиотека имени Ленина', 'Кропоткинская'): 2,
    ('Кропоткинская', 'Парк культуры1'): 2,
    ('Парк культуры1', 'Фрунзенская'): 3,
    ('Фрунзенская', 'Спортивная'): 2,
    ('Спортивная', 'Воробьёвы горы'): 3,
    ('Воробьёвы горы', 'Университет'): 3,
    ('Университет', 'Проспект Вернадского1'): 3,
    ('Проспект Вернадского1', 'Юго-Западная'): 3,
    ('Юго-Западная', 'Тропарёво'): 4,
    ('Тропарёво', 'Румянцево'): 3,
    ('Румянцево', 'Саларьево'): 3,
    ('Саларьево', 'Филатов Луг'): 4,
    ('Филатов Луг', 'Прокшино'): 3,
    ('Прокшино', 'Ольховая'): 4,
    ('Ольховая', 'Коммунарка'): 2,
    # line 1 transitions
    ('Комсомольская1', 'Комсомольская5'): 5,
    ('Чистые пруды', 'Тургеневская'): 3,
    ('Чистые пруды', 'Сретенский бульвар'): 4,
    ('Лубянка', 'Кузнецкий Мост'): 4,
    ('Охотный Ряд', 'Театральная'): 5,
    ('Библиотека имени Ленина', 'Арбатская'): 4,
    ('Библиотека имени Ленина', 'Боровицкая'): 4,
    ('Парк культуры1', 'Парк культуры5'): 4,
    ('Проспект Вернадского1', 'Проспект Вернадского11'): 4,
    # line 2
    ('Ховрино', 'Беломорская'): 2,
    ('Беломорская', 'Речной вокзал'): 2,
    ('Речной вокзал', 'Водный стадион'): 3,
    ('Водный стадион', 'Войковская'): 3,
    ('Войковская', 'Сокол'): 3,
    ('Сокол', 'Аэропорт'): 2,
    ('Аэропорт', 'Динамо'): 3,
    ('Динамо', 'Белорусская2'): 3,
    ('Белорусская2', 'Маяковская'): 3,
    ('Маяковская', 'Тверская'): 3,
    ('Тверская', 'Театральная'): 3,
    ('Театральная', 'Новокузнецкая'): 3,
    ('Новокузнецкая', 'Павелецкая2'): 2,
    ('Павелецкая2', 'Автозаводская'): 4,

    ('Автозаводская', 'Технопарк'): 4,
    ('Технопарк', 'Коломенская'): 4,
    ('Коломенская', 'Каширская'): 4,
    ('Каширская', 'Кантемировская'): 4,
    ('Кантемировская', 'Царицыно'): 4,
    ('Царицыно', 'Орехово'): 4,

    ('Орехово', 'Домодедовская'): 3,
    ('Домодедовская', 'Красногвардейская'): 3,
    ('Красногвардейская', 'Алма-Атинская'): 6,
    # line 2 transitions
    ('Динамо', 'Петровский парк'): 4,
    ('Белорусская2', 'Белорусская5'): 4,
    ('Тверская', 'Пушкинская'): 4,
    ('Тверская', 'Чеховская'): 4,
    ('Театральная', 'Охотный Ряд'): 4,
    ('Театральная', 'Площадь Революции'): 4,
    ('Новокузнецкая', 'Третьяковская6'): 4,
    ('Новокузнецкая', 'Третьяковская8'): 4,
    ('Павелецкая2', 'Павелецкая5'): 4,
    ('Красногвардейская', 'Зябликово'): 4,
    # line 3
    ('Пятницкое шоссе', 'Митино'): 2,
    ('Митино', 'Волоколамская'): 3,
    ('Волоколамская', 'Мякинино'): 2,
    ('Мякинино', 'Строгино'): 4,
    ('Строгино', 'Крылатское'): 8,
    ('Крылатское', 'Молодёжная'): 3,
    ('Молодёжная', 'Кунцевская3'): 3,
    ('Кунцевская3', 'Славянский бульвар'): 3,
    ('Славянский бульвар', 'Парк Победы3'): 4,
    ('Парк Победы3', 'Киевская3'): 5,
    ('Киевская3', 'Смоленская3'): 2,
    ('Смоленская3', 'Арбатская3'): 2,
    ('Арбатская3', 'Площадь Революции'): 2,
    ('Площадь Революции', 'Курская3'): 3,
    ('Курская3', 'Бауманская'): 3,
    ('Бауманская', 'Электрозаводская3'): 2,
    ('Электрозаводская3', 'Семёновская'): 2,
    ('Семёновская', 'Партизанская'): 3,
    ('Партизанская', 'Измайловская'): 3,
    ('Измайловская', 'Первомайская'): 3,
    ('Первомайская', 'Щёлковская'): 2,
    # line 3 transitions
    ('Арбатская3', 'Библиотека имени Ленина'): 5,
    ('Площадь Революции', 'Театральная'): 5,
    ('Кунцевская3', 'Кунцевская4'): 3,
    ('Киевская3', 'Киевская4'): 6,
    ('Арбатская3', 'Александровский сад'): 3,
    ('Киевская3', 'Киевская4A'): 6,
    ('Киевская3', 'Киевская5'): 3,
    ('Курская3', 'Курская5'): 4,
    ('Парк Победы3', 'Парк Победы8A'): 2,
    ('Арбатская3', 'Боровицкая'): 4,
    ('Курская3', 'Чкаловская'): 4,
    ('Кунцевская3', 'Кунцевская11'): 5,
    ('Электрозаводская3', 'Электрозаводская15'): 8,
    # line 4
    ('Кунцевская4', 'Пионерская'): 2,
    ('Пионерская', 'Филёвский парк'): 2,
    ('Филёвский парк', 'Багратионовская'): 2,
    ('Багратионовская', 'Фили'): 3,
    ('Фили', 'Кутузовская'): 3,
    ('Кутузовская', 'Студенческая'): 2,
    ('Студенческая', 'Киевская4'): 3,
    ('Киевская4', 'Смоленская4'): 3,
    ('Смоленская4', 'Арбатская4'): 2,
    ('Арбатская4', 'Александровский сад'): 2,
    # line 4 transitions
    ('Александровский сад', 'Библиотека имени Ленина'): 3,
    ('Киевская4', 'Киевская3'): 6,
    ('Киевская4', 'Киевская4A'): 0,
    ('Киевская4', 'Киевская5'): 6,
    ('Александровский сад', 'Арбатская3'): 3,
    ('Кунцевская4', 'Кунцевская3'): 3,
    # line 4A
    ('Киевская4A', 'Выставочная'): 8,
    ('Выставочная', 'Международная'): 2,
    # line 4A transitions
    ('Киевская4A', 'Киевская3'): 6,
    ('Киевская4A', 'Киевская4'): 0,
    ('Выставочная', 'Деловой центр8A'): 3,
    ('Выставочная', 'Деловой центр11A'): 3,
    # line 5
    ('Проспект Мира5', 'Новослободская'): 3,
    ('Новослободская', 'Белорусская5'): 2,
    ('Белорусская5', 'Краснопресненская'): 3,
    ('Краснопресненская', 'Киевская5'): 3,
    ('Киевская5', 'Парк культуры5'): 3,
    ('Парк культуры5', 'Октябрьская5'): 2,
    ('Октябрьская5', 'Добрынинская'): 2,
    ('Добрынинская', 'Павелецкая5'): 2,
    ('Павелецкая5', 'Таганская5'): 2,
    ('Таганская5', 'Курская5'): 3,
    ('Курская5', 'Комсомольская5'): 3,
    ('Комсомольская5', 'Проспект Мира5'): 3,
    # line 5 transitions
    ('Проспект Мира5', 'Проспект Мира6'): 4,
    ('Октябрьская5', 'Октябрьская6'): 3,
    ('Краснопресненская', 'Баррикадная'): 3,
    ('Таганская5', 'Таганская7'): 3,
    ('Таганская5', 'Марксистская'): 3,
    ('Курская5', 'Чкаловская'): 6,
    # line 6
    ('Медведково', 'Бабушкинская'): 3,
    ('Бабушкинская', 'Свиблово'): 2,
    ('Свиблово', 'Ботанический сад'): 2,
    ('Ботанический сад', 'ВДНХ'): 4,
    ('ВДНХ', 'Алексеевская'): 2,
    ('Алексеевская', 'Рижская'): 2,
    ('Рижская', 'Проспект Мира6'): 3,
    ('Проспект Мира6', 'Сухаревская'): 2,
    ('Сухаревская', 'Тургеневская'): 2,
    ('Тургеневская', 'Китай-город6'): 2,
    ('Китай-город6', 'Третьяковская6'): 3,
    ('Третьяковская6', 'Октябрьская6'): 3,
    ('Октябрьская6', 'Шаболовская'): 2,
    ('Шаболовская', 'Ленинский проспект'): 3,
    ('Ленинский проспект', 'Академическая'): 3,
    ('Академическая', 'Профсоюзная'): 2,
    ('Профсоюзная', 'Новые Черёмушки'): 2,
    ('Новые Черёмушки', 'Калужская'): 2,
    ('Калужская', 'Беляево'): 3,
    ('Беляево', 'Коньково'): 2,
    ('Коньково', 'Тёплый Стан'): 3,
    ('Тёплый Стан', 'Ясенево'): 3,
    ('Ясенево', 'Новоясеневская'): 2,
    # line 6 transitions
    ('Китай-город6', 'Китай-город7'): 2,
    ('Третьяковская6', 'Третьяковская8'): 2,
    ('Тургеневская', 'Сретенский бульвар'): 3,
    ('Калужская', 'Воронцовская'): 4,
    ('Новоясеневская', 'Битцевский парк'): 3,
    # line 7
    ('Планерная', 'Сходненская'): 3,
    ('Сходненская', 'Тушинская'): 2,
    ('Тушинская', 'Спартак'): 2,
    ('Спартак', 'Щукинская'): 4,
    ('Щукинская', 'Октябрьское Поле'): 2,
    ('Октябрьское Поле', 'Полежаевская'): 2,
    ('Полежаевская', 'Беговая'): 3,
    ('Беговая', 'Улица 1905 года'): 2,
    ('Улица 1905 года', 'Баррикадная'): 2,
    ('Баррикадная', 'Пушкинская'): 2,
    ('Пушкинская', 'Кузнецкий Мост'): 3,
    ('Кузнецкий Мост', 'Китай-город7'): 3,
    ('Китай-город7', 'Таганская7'): 2,
    ('Таганская7', 'Пролетарская'): 3,
    ('Пролетарская', 'Волгоградский проспект'): 3,
    ('Волгоградский проспект', 'Текстильщики'): 2,
    ('Текстильщики', 'Кузьминки'): 2,
    ('Кузьминки', 'Рязанский проспект'): 2,
    ('Рязанский проспект', 'Выхино'): 3,
    ('Выхино', 'Лермонтовский проспект'): 2,
    ('Лермонтовский проспект', 'Жулебино'): 3,
    ('Жулебино', 'Котельники'): 3,
    # line 7 transitions
    ('Таганская7', 'Марксистская'): 4,
    ('Пушкинская', 'Чеховская'): 4,
    ('Пролетарская', 'Крестьянская застава'): 5,
    ('Полежаевская', 'Хорошёвская11'): 3,
    ('Полежаевская', 'Хорошёвская11A'): 3,
    # line 8
    ('Третьяковская8', 'Марксистская'): 3,
    ('Марксистская', 'Площадь Ильича'): 3,
    ('Площадь Ильича', 'Авиамоторная8'): 3,
    ('Авиамоторная8', 'Шоссе Энтузиастов'): 3,
    ('Шоссе Энтузиастов', 'Перово'): 3,
    ('Перово', 'Новогиреево'): 3,
    ('Новогиреево', 'Новокосино'): 4,
    # line 8 transitions
    ('Площадь Ильича', 'Римская'): 3,
    ('Авиамоторная8', 'Авиамоторная15'): 12,
    # line 8A
    ('Рассказовка', 'Новопеределкино'): 3,
    ('Новопеределкино', 'Боровское шоссе'): 3,
    ('Боровское шоссе', 'Солнцево'): 4,
    ('Солнцево', 'Говорово'): 4,
    ('Говорово', 'Озёрная'): 4,
    ('Озёрная', 'Мичуринский проспект8A'): 5,
    ('Мичуринский проспект8A', 'Раменки'): 4,
    ('Раменки', 'Ломоносовский проспект'): 3,
    ('Ломоносовский проспект', 'Минская'): 5,
    ('Минская', 'Парк Победы8A'): 4,
    ('Парк Победы8A', 'Деловой центр8A'): 5,
    # line 8A transitions
    ('Мичуринский проспект8A', 'Мичуринский проспект11'): 5,
    ('Деловой центр8A', 'Деловой центр11A'): 3,
    # line 9
    ('Алтуфьево', 'Бибирево'): 3,
    ('Бибирево', 'Отрадное'): 3,
    ('Отрадное', 'Владыкино'): 3,
    ('Владыкино', 'Петровско-Разумовская9'): 2,
    ('Петровско-Разумовская9', 'Тимирязевская'): 3,
    ('Тимирязевская', 'Дмитровская'): 2,
    ('Дмитровская', 'Савёловская9'): 2,
    ('Савёловская9', 'Менделеевская'): 2,
    ('Менделеевская', 'Цветной бульвар'): 3,
    ('Цветной бульвар', 'Чеховская'): 2,
    ('Чеховская', 'Боровицкая'): 3,
    ('Боровицкая', 'Полянка'): 2,
    ('Полянка', 'Серпуховская'): 2,
    ('Серпуховская', 'Тульская'): 3,
    ('Тульская', 'Нагатинская'): 4,
    ('Нагатинская', 'Нагорная'): 2,
    ('Нагорная', 'Нахимовский проспект'): 2,
    ('Нахимовский проспект', 'Севастопольская'): 2,
    ('Севастопольская', 'Чертановская'): 2,
    ('Чертановская', 'Южная'): 3,
    ('Южная', 'Пражская'): 2,
    ('Пражская', 'Улица Академика Янгеля'): 2,
    ('Улица Академика Янгеля', 'Аннино'): 2,
    ('Аннино', 'Бульвар Дмитрия Донского'): 3,
    # line 9 transitions
    ('Петровско-Разумовская9', 'Петровско-Разумовская10'): 2,
    ('Цветной бульвар', 'Трубная'): 4,
    ('Савёловская9', 'Савёловская11'): 3,
    ('Севастопольская', 'Каховская'): 2,
    ('Бульвар Дмитрия Донского', 'Улица Старокачаловская'): 3,
    # line 10
    ('Селигерская', 'Верхние Лихоборы'): 2,
    ('Верхние Лихоборы', 'Окружная'): 2,
    ('Окружная', 'Петровско-Разумовская10'): 2,
    ('Петровско-Разумовская10', 'Фонвизинская'): 3,
    ('Фонвизинская', 'Бутырская'): 2,
    ('Бутырская', 'Марьина Роща'): 3,
    ('Марьина Роща', 'Достоевская'): 3,
    ('Достоевская', 'Трубная'): 3,
    ('Трубная', 'Сретенский бульвар'): 3,
    ('Сретенский бульвар', 'Чкаловская'): 3,
    ('Чкаловская', 'Римская'): 3,
    ('Римская', 'Крестьянская застава'): 3,
    ('Крестьянская застава', 'Дубровка'): 2,
    ('Дубровка', 'Кожуховская'): 3,
    ('Кожуховская', 'Печатники'): 4,
    ('Печатники', 'Волжская'): 3,
    ('Волжская', 'Люблино'): 3,
    ('Люблино', 'Братиславская'): 3,
    ('Братиславская', 'Марьино'): 2,
    ('Марьино', 'Борисово'): 3,
    ('Борисово', 'Шипиловская'): 2,
    ('Шипиловская', 'Зябликово'): 2,
    # line 11
    ('Савёловская11', 'Петровский парк'): 5,
    ('Петровский парк', 'ЦСКА'): 5,
    ('ЦСКА', 'Хорошёвская11'): 5,
    ('Хорошёвская11', 'Народное Ополчение'): 6,
    ('Народное Ополчение', 'Мнёвники'): 5,
    ('Мнёвники', 'Терехово'): 5,
    ('Терехово', 'Кунцевская11'): 5,
    ('Кунцевская11', 'Давыдково'): 5,
    ('Давыдково', 'Аминьевская'): 5,
    ('Аминьевская', 'Мичуринский проспект11'): 5,
    ('Мичуринский проспект11', 'Проспект Вернадского11'): 5,
    ('Проспект Вернадского11', 'Новаторская'): 4,
    ('Новаторская', 'Воронцовская'): 5,
    ('Воронцовская', 'Зюзино'): 5,
    ('Зюзино', 'Каховская'): 4,
    # line 11 transitions
    ('Хорошёвская11', 'Хорошёвская11A'): 0,
    # line 11A
    ('Хорошёвская11A', 'Шелепиха'): 8,
    ('Шелепиха', 'Деловой центр11A'): 5,
    # line 12
    ('Битцевский парк', 'Лесопарковая'): 3,
    ('Лесопарковая', 'Улица Старокачаловская'): 3,
    ('Улица Старокачаловская', 'Улица Скобелевская'): 5,
    ('Улица Скобелевская', 'Бульвар Адмирала Ушакова'): 1,
    ('Бульвар Адмирала Ушакова', 'Улица Горчакова'): 2,
    ('Улица Горчакова', 'Бунинская аллея'): 2,
    # line 15
    ('Электрозаводская15', 'Лефортово'): 3,
    ('Лефортово', 'Авиамоторная15'): 2,
    ('Авиамоторная15', 'Нижегородская'): 3,
    ('Нижегородская', 'Стахановская'): 2,
    ('Стахановская', 'Окская'): 2,
    ('Окская', 'Юго-Восточная'): 3,
    ('Юго-Восточная', 'Косино'): 2,
    ('Косино', 'Улица Дмитриевского'): 6,
    ('Улица Дмитриевского', 'Лухмановская'): 1,
    ('Лухмановская', 'Некрасовка'): 2,
}


def determining_the_time(route_: list) -> int:
    summ = 0
    try:
        for j in route_:
            try:
                if j != route_[-1]:
                    summ += data[(j, route_[route_.index(j) + 1])]
            except KeyError:
                if j != route_[-1]:
                    summ += data[(route_[route_.index(j) + 1], j)]
        return summ
    except KeyError:
        return 500


if __name__ == '__main__':
    route = [['Красносельская', ]]
    print(determining_the_time(['Сокольники', 'Красносельская']))
    route.sort(key=determining_the_time)
    print(route)
