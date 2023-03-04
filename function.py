# словарь всех станций
lines = {
    1: ['Бульвар Рокоссовского', 'Черкизовская', 'Преображенская площадь', 'Сокольники',
       'Красносельская', 'Комсомольская1', 'Красные Ворота', 'Чистые пруды',
       'Лубянка', 'Охотный Ряд', 'Библиотека имени Ленина', 'Кропоткинская',
       'Парк культуры1', 'Фрунзенская', 'Спортивная', 'Воробьёвы горы',
       'Университет', 'Проспект Вернадского1', 'Юго-Западная', 'Тропарёво',
       'Румянцево', 'Саларьево', 'Филатов Луг', 'Прокшино',
       'Ольховая', 'Коммунарка', ],

    2: ['Ховрино', 'Беломорская', 'Речной вокзал', 'Водный стадион', 'Войковская', 'Сокол', 'Аэропорт', 'Динамо',
         'Белорусская2', 'Маяковская', 'Тверская', 'Театральная', 'Новокузнецкая', 'Павелецкая2', 'Автозаводская',
         'Технопарк', 'Коломенская', 'Каширская', 'Кантемировская', 'Царицыно', 'Орехово', 'Домодедовская',
         'Красногвардейская', 'Алма-Атинская', ],

    3: ['Пятницкое шоссе', 'Митино', 'Волоколамская', 'Мякинино', 'Строгино', 'Крылатское', 'Молодёжная', 'Кунцевская3',
        'Славянский бульвар', 'Парк Победы3', 'Киевская3', 'Смоленская3', 'Арбатская3', 'Площадь Революции', 'Курская3',
        'Бауманская', 'Электрозаводская3', 'Семёновская', 'Партизанская', 'Измайловская', 'Первомайская', 'Щёлковская'],

    4: ['Кунцевская4', 'Пионерская', 'Филёвский парк', 'Багратионовская', 'Фили', 'Кутузовская', 'Студенческая',
        'Киевская4', 'Смоленская4', 'Арбатская4', 'Александровский сад'],

    '4A': ['Киевская4A', 'Выставочная', 'Международная'],

    5: ['Проспект Мира5', 'Новослободская', 'Белорусская5', 'Краснопресненская', 'Киевская5', 'Парк культуры5',
        'Октябрьская5', 'Добрынинская', 'Павелецкая5', 'Таганская5', 'Курская5', 'Комсомольская5'],

    6: ['Медведково', 'Бабушкинская', 'Свиблово', 'Ботанический сад', 'ВДНХ', 'Алексеевская', 'Рижская',
        'Проспект Мира6', 'Сухаревская', 'Тургеневская', 'Китай-город6', 'Третьяковская6', 'Октябрьская6',
        'Шаболовская', 'Ленинский проспект', 'Академическая', 'Профсоюзная', 'Новые Черёмушки', 'Калужская', 'Беляево',
        'Коньково', 'Тёплый Стан', 'Ясенево', 'Новоясеневская'],

    7: ['Планерная', 'Сходненская', 'Тушинская', 'Спартак', 'Щукинская', 'Октябрьское Поле', 'Полежаевская', 'Беговая',
        'Улица 1905 года', 'Баррикадная', 'Пушкинская', 'Кузнецкий Мост', 'Китай-город7', 'Таганская7', 'Пролетарская',
        'Волгоградский проспект', 'Текстильщики', 'Кузьминки', 'Рязанский проспект', 'Выхино', 'Лермонтовский проспект',
        'Жулебино', 'Котельники'],

    8: ['Третьяковская8', 'Марксистская', 'Площадь Ильича', 'Авиамоторная8', 'Шоссе Энтузиастов', 'Перово',
        'Новогиреево', 'Новокосино'],

    '8A': ['Рассказовка', 'Новопеределкино', 'Боровское шоссе', 'Солнцево', 'Говорово', 'Озёрная',
           'Мичуринский проспект8A', 'Раменки', 'Ломоносовский проспект', 'Минская', 'Парк Победы8A', 'Деловой центр8A'],

    9: ['Алтуфьево', 'Бибирево', 'Отрадное', 'Владыкино', 'Петровско-Разумовская9', 'Тимирязевская', 'Дмитровская',
        'Савёловская9', 'Менделеевская', 'Цветной бульвар', 'Чеховская', 'Боровицкая', 'Полянка', 'Серпуховская',
        'Тульская', 'Нагатинская', 'Нагорная', 'Нахимовский проспект', 'Севастопольская', 'Чертановская', 'Южная',
        'Пражская', 'Улица Академика Янгеля', 'Аннино', 'Бульвар Дмитрия Донского'],

    10: ['Селигерская', 'Верхние Лихоборы', 'Окружная', 'Петровско-Разумовская10', 'Фонвизинская', 'Бутырская',
         'Марьина Роща', 'Достоевская', 'Трубная', 'Сретенский бульвар', 'Чкаловская', 'Римская',
         'Крестьянская застава', 'Дубровка', 'Кожуховская', 'Печатники', 'Волжская', 'Люблино', 'Братиславская',
         'Марьино', 'Борисово', 'Шипиловская', 'Зябликово'],

    11: ['Савёловская11', 'Петровский парк', 'ЦСКА', 'Хорошёвская11', 'Народное Ополчение', 'Мнёвники', 'Терехово',
         'Кунцевская11', 'Давыдково', 'Аминьевская', 'Мичуринский проспект11', 'Проспект Вернадского11', 'Новаторская',
         'Воронцовская', 'Зюзино', 'Каховская'],

    '11A': ['Хорошёвская11A', 'Шелепиха', 'Деловой центр11A'],

    12: ['Битцевский парк', 'Лесопарковая', 'Улица Старокачаловская', 'Улица Скобелевская', 'Бульвар Адмирала Ушакова',
         'Улица Горчакова', 'Бунинская аллея'],

    15: ['Электрозаводская15', 'Лефортово', 'Авиамоторная15', 'Нижегородская', 'Стахановская', 'Окская',
         'Юго-Восточная', 'Косино', 'Улица Дмитриевского', 'Лухмановская', 'Некрасовка'],
}
five2 = ['Октябрьская5', 'Добрынинская', 'Павелецкая5', 'Таганская5', 'Курская5', 'Комсомольская5', 'Проспект Мира5',
         'Новослободская', 'Белорусская5', 'Краснопресненская', 'Киевская5', 'Парк культуры5']
# словарь всех пересадок
trans = {
    1: {
        2: [['Охотный Ряд', 'Театральная']],
        3: [['Библиотека имени Ленина', 'Арбатская3']],
        4: [['Библиотека имени Ленина', 'Александровский сад']],
        5: [['Парк культуры1', 'Парк культуры5'], ['Комсомольская1', 'Комсомольская5']],
        6: [['Чистые пруды', 'Тургеневская']],
        7: [['Лубянка', 'Кузнецкий Мост']],
        9: [['Библиотека имени Ленина', 'Боровицкая']],
        10: [['Чистые пруды', 'Сретенский бульвар']],
        11: [['Проспект Вернадского1', 'Проспект Вернадского11']]
    },
    2: {
        1: [['Театральная', 'Охотный Ряд']],
        3: [['Театральная', 'Площадь Революции']],
        5: [['Белорусская2', 'Белорусская5'], ['Павелецкая2', 'Павелецкая5']],
        6: [['Новокузнецкая', 'Третьяковская6']],
        7: [['Тверская', 'Пушкинская']],
        8: [['Новокузнецкая', 'Третьяковская8']],
        9: [['Тверская', 'Чеховская']],
        10: [['Красногвардейская', 'Зябликово']],
        11: [['Динамо', 'Петровский парк']]
    },
    3: {
        1: [['Арбатская3', 'Библиотека имени Ленина']],
        2: [['Площадь Революции', 'Театральная']],
        4: [['Кунцевская3', 'Кунцевская4'], ['Киевская3', 'Киевская4'], ['Арбатская3', 'Александровский сад']],
        '4A': [['Киевская3', 'Киевская4A']],
        5: [['Киевская3', 'Киевская5'], ['Курская3', 'Курская5']],
        '8A': [['Парк Победы3', 'Парк Победы8A']],
        9: [['Арбатская3', 'Боровицкая']],
        10: [['Курская3', 'Чкаловская']],
        11: [['Кунцевская3', 'Кунцевская11']],
        15: [['Электрозаводская3', 'Электрозаводская15']],
    },
    4: {
        1: [['Александровский сад', 'Библиотека имени Ленина']],
        3: [['Киевская4', 'Киевская3'], ['Александровский сад', 'Арбатская3'], ['Кунцевская4', 'Кунцевская3']],
        '4A': [['Киевская4', 'Киевская4A']],
        5: [['Киевская4', 'Киевская5']],
        11: [['Кунцевская4', 'Кунцевская11']],
    },
    '4A': {
        3: [['Киевская4A', 'Киевская3']],
        4: [['Киевская4A', 'Киевская4']],
        '8A': [['Выставочная', 'Деловой центр8A']],
        '11A': [['Выставочная', 'Деловой центр11A']],
    },
    5: {
        1: [['Комсомольская5', 'Комсомольская1'], ['Парк культуры5', 'Парк культуры1']],
        2: [['Белорусская5', 'Белорусская2'], ['Павелецкая5', 'Павелецкая2']],
        3: [['Киевская5', 'Киевская3'], ['Курская5', 'Курская3']],
        4: [['Киевская5', 'Киевская4']],
        6: [['Проспект Мира5', 'Проспект Мира6'], ['Октябрьская5', 'Октябрьская6']],
        7: [['Краснопресненская', 'Баррикадная'], ['Таганская5', 'Таганская7']],
        8: [['Таганская5', 'Марксистская']],
        9: [['Новослободская', 'Менделеевская'], ['Добрынинская', 'Серпуховская']],
        10: [['Курская5', 'Чкаловская']],
    },
    6: {
        1: [['Тургеневская', 'Чистые пруды']],
        2: [['Третьяковская6', 'Новокузнецкая']],
        5: [['Проспект Мира6', 'Проспект Мира5'], ['Октябрьская6', 'Октябрьская5']],
        7: [['Китай-город6', 'Китай-город7']],
        8: [['Третьяковская6', 'Третьяковская8']],
        10: [['Тургеневская', 'Сретенский бульвар']],
        11: [['Калужская', 'Воронцовская']],
        12: [['Новоясеневская', 'Битцевский парк']]
    },
    7: {
        1: [['Кузнецкий Мост', 'Лубянка']],
        2: [['Пушкинская', 'Тверская']],
        5: [['Баррикадная', 'Краснопресненская'], ['Таганская7', 'Таганская5']],
        6: [['Китай-город7', 'Китай-город6']],
        8: [['Таганская7', 'Марксистская']],
        9: [['Пушкинская', 'Чеховская']],
        10: [['Пролетарская', 'Крестьянская застава']],
        11: [['Полежаевская', 'Хорошёвская11']],
        '11A': [['Полежаевская', 'Хорошёвская11A']],
    },
    8: {
        2: [['Третьяковская8', 'Новокузнецкая']],
        5: [['Марксистская', 'Таганская5']],
        6: [['Третьяковская8', 'Третьяковская6']],
        7: [['Марксистская', 'Таганская7']],
        10: [['Площадь Ильича', 'Римская']],
        15: [['Авиамоторная8', 'Авиамоторная15']],
    },
    '8A': {
        3: [['Парк Победы8A', 'Парк Победы3']],
        '4A': [['Деловой центр8A', 'Выставочная']],
        11: [['Мичуринский проспект8A', 'Мичуринский проспект11']],
        '11A': [['Деловой центр8A', 'Деловой центр11A']]
    },
    9: {
        1: [['Боровицкая', 'Библиотека имени Ленина']],
        2: [['Чеховская', 'Тверская']],
        3: [['Боровицкая', 'Арбатская3']],
        4: [['Боровицкая', 'Александровский сад']],
        5: [['Менделеевская', 'Новослободская'], ['Серпуховская', 'Добрынинская']],
        7: [['Чеховская', 'Пушкинская']],
        10: [['Петровско-Разумовская9', 'Петровско-Разумовская10'], ['Цветной бульвар', 'Трубная']],
        11: [['Савёловская9', 'Савёловская11'], ['Севастопольская', 'Каховская']],
        12: [['Бульвар Дмитрия Донского', 'Улица Старокачаловская']]
    },
    10: {
        1: [['Сретенский бульвар', 'Чистые пруды']],
        2: [['Зябликово', 'Красногвардейская']],
        3: [['Чкаловская', 'Курская3']],
        5: [['Чкаловская', 'Курская5']],
        6: [['Сретенский бульвар', 'Тургеневская']],
        7: [['Крестьянская застава', 'Пролетарская']],
        8: [['Римская', 'Площадь Ильича']],
        9: [['Петровско-Разумовская10', 'Петровско-Разумовская9']]
    },
    11: {
        1: [['Проспект Вернадского11', 'Проспект Вернадского1']],
        2: [['Петровский парк', 'Динамо']],
        3: [['Кунцевская11', 'Кунцевская3']],
        4: [['Кунцевская11', 'Кунцевская4']],
        6: [['Воронцовская', 'Калужская']],
        7: [['Хорошёвская11', 'Полежаевская']],
        '8A': [['Мичуринский проспект11', 'Мичуринский проспект8A']],
        9: [['Савёловская11', 'Савёловская9'], ['Каховская', 'Севастопольская']],
        '11A': [['Хорошёвская11', 'Хорошёвская11A']]
    },
    '11A': {
        '4A': [['Деловой центр11A', 'Выставочная']],
        7: [['Хорошёвская11A', 'Полежаевская']],
        '8A': [['Деловой центр11A', 'Деловой центр8A']],
        11: [['Хорошёвская11A', 'Хорошёвская11']]
    },
    12: {
        6: [['Битцевский парк', 'Новоясеневская']],
        9: [['Улица Старокачаловская', 'Бульвар Дмитрия Донского']]
    },
    15: {
        3: [['Электрозаводская15', 'Электрозаводская3']],
        7: [['Косино', 'Лермонтовский проспект']],
        8: [['Авиамоторная15', 'Авиамоторная8']],
    }
}


# алгоритм построения маршрута НАХУЙ
def plotting_a_route(station1: str, line1: int or str, station2: str, line2: int or str) -> list:
    print(station1, line1, station2, line2)
    global lines, trans
    line_fixed_1 = line1
    line_fixed_2 = line2
    line_resault = []
    # маршрут для одной линии
    try:
        line = lines[line1]
        if line1 == 5:
            match line[line.index(station1):line.index(station2):]:
                case []:
                    line = line[::-1]
                    line_resault.append(line[line.index(station1):line.index(station2) + 1:])
                case _:
                    line_resault.append(line[line.index(station1):line.index(station2) + 1:])
            line = five2
            match line[line.index(station1):line.index(station2):]:
                case []:
                    line = line[::-1]
                    line_resault.append(line[line.index(station1):line.index(station2) + 1:])
                case _:
                    line_resault.append(line[line.index(station1):line.index(station2) + 1:])
        else:
            match line[line.index(station1):line.index(station2):]:
                case []:
                    line = line[::-1]
                    line_resault.append(line[line.index(station1):line.index(station2) + 1:])
                case _:
                    line_resault.append(line[line.index(station1):line.index(station2) + 1:])
    except ValueError:
        pass
    '''
    # маршрут для 4 линии
    if line1 == 4 and line2 == '4A':
        line = lines[line1]
        if line[line.index(station1):8:] == []:
            line = line[::-1]
            line = line[line.index(station1):4:]
            for i in lines[line2]:
                    line.append(i)
        else:
            line = lines[line1][line.index(station1):8:]
            for i in lines[line2]:
                    line.append(i)
        line_resault.append(line[:line.index(station2) + 1:])
    elif line1 == '4A' and line2 == 4:
        line = lines[line1]
        if line[line.index(station1):1:] == []:
            line = line[::-1]
            line = line[line.index(station1):3:]
            if 7 > lines[line2].index(station2):
                for i in lines[line2][:8:][::-1]:
                        line.append(i)
            else:
                for i in lines[line2][7:lines[line2].index(station2) + 1:]:
                        line.append(i)
        else:
            line = lines[line1][line.index(station1):1:]
            if 7 > lines[line2].index(station2):
                for i in lines[line2][:8:][::-1]:
                    line.append(i)
            else:
                for i in lines[line2][7:lines[line2].index(station2) + 1:]:
                    line.append(i)
        line_resault.append(line[:line.index(station2) + 1:])'''
    # маршруты двух вариантов (больше одной линии)
    # находим маршрут с одной пересадкой
    try:
        tr_ = trans[line_fixed_1][line_fixed_2]
        for j in tr_:
            tr = [j]
            # находим массив станций для 1-ой линии
            if line1 == 5:
                for line in [lines[line1], five2]:
                    try:
                        match line[line.index(station1):line.index(tr[0][0]) + 1:]:
                            case []:
                                line = line[line.index(station1):line.index(tr[0][0]):-1]
                                line.append(tr[0][0])
                            case _:
                                line = line[line.index(station1):line.index(tr[0][0]) + 1:]
                        # находим массив станций для 2-ой линии
                        line_ = lines[line2]
                        match line_[line_.index(tr[0][1]):line_.index(station2) + 1:]:
                            case []:
                                line_ = line_[line_.index(tr[0][1]):line_.index(station2):-1]
                                line_.append(station2)
                            case _:
                                line_ = line_[line_.index(tr[0][1]):line_.index(station2) + 1:]
                        line_resault.append(line + line_)
                    except ValueError:
                        continue
            if line2 == 5:
                for line_ in [lines[line1], five2]:
                    try:
                        line = lines[line1]
                        match line[line.index(station1):line.index(tr[0][0]) + 1:]:
                            case []:
                                line = line[line.index(station1):line.index(tr[0][0]):-1]
                                line.append(tr[0][0])
                            case _:
                                line = line[line.index(station1):line.index(tr[0][0]) + 1:]
                        # находим массив станций для 2-ой линии
                        match line_[line_.index(tr[0][1]):line_.index(station2) + 1:]:
                            case []:
                                line_ = line_[line_.index(tr[0][1]):line_.index(station2):-1]
                                line_.append(station2)
                            case _:
                                line_ = line_[line_.index(tr[0][1]):line_.index(station2) + 1:]
                        line_resault.append(line + line_)
                    except ValueError:
                        continue
            else:
                line = lines[line1]
                match line[line.index(station1):line.index(tr[0][0]) + 1:]:
                    case []:
                        line = line[line.index(station1):line.index(tr[0][0]):-1]
                        line.append(tr[0][0])
                    case _:
                        line = line[line.index(station1):line.index(tr[0][0]) + 1:]
                # находим массив станций для 2-ой линии
                line_ = lines[line2]
                match line_[line_.index(tr[0][1]):line_.index(station2) + 1:]:
                    case []:
                        line_ = line_[line_.index(tr[0][1]):line_.index(station2):-1]
                        line_.append(station2)
                    case _:
                        line_ = line_[line_.index(tr[0][1]):line_.index(station2) + 1:]
                line_resault.append(line + line_)
    except KeyError:
        pass
    # находим все маршруты с двумя пересадками
    try:
        tr1 = []
        tr2 = []
        #
        for i in trans[line1].keys():
            try:
                tr1 = trans[line_fixed_1][i]
                tr2 = trans[i][line_fixed_2]
                line2, line3 = i, line_fixed_2
                line = lines[line1]
                if len(tr1) != 1:
                    size = []
                    for j in tr1:
                        try:
                            if line_fixed_1 == 5:
                                for line in [lines[line1], five2]:
                                    match line[line.index(station1):line.index(j[0]) + 1:]:
                                        case []:
                                            l = line[line.index(station1):line.index(j[0]):-1]
                                            l.append(j[0])
                                            size.append(len(l))
                                        case None:
                                            size.append(1)
                                        case _:
                                            size.append(len(line[line.index(station1):line.index(j[0]) + 1:]))
                            else:
                                match line[line.index(station1):line.index(j[0]) + 1:]:
                                    case []:
                                        l = line[line.index(station1):line.index(j[0]):-1]
                                        l.append(j[0])
                                        size.append(len(l))
                                    case None:
                                        size.append(1)
                                    case _:
                                        size.append(len(line[line.index(station1):line.index(j[0]) + 1:]))
                        except ValueError:
                            continue
                    min_tr = size.index(min(size))
                    tr1 = [tr1[min_tr]]
                    print(tr1)
                else:
                    if tr1[0][0] == tr2[0][1]:
                        continue
                line_ = lines[line2]
                if len(tr2) != 1:
                    size = []
                    for j in tr2:
                        try:
                            if j[1] != tr1[0][0]:
                                if line2 == 5:
                                    for line_ in [lines[line2], five2]:
                                        match line_[line_.index(tr1[0][1]):line_.index(j[0]) + 1:]:
                                            case []:
                                                l = line_[line_.index(tr1[0][1]):line_.index(j[0]):-1]
                                                l.append(j[0])
                                                size.append(len(l))
                                            case None:
                                                size.append(1)
                                            case _:
                                                size.append(len(line_[line_.index(tr1[0][1]):line_.index(j[0]) + 1:]))
                                else:
                                    match line_[line_.index(tr1[0][1]):line_.index(j[0]) + 1:]:
                                        case []:
                                            l = line_[line_.index(tr1[0][1]):line_.index(j[0]):-1]
                                            l.append(j[0])
                                            size.append(len(l))
                                        case None:
                                            size.append(1)
                                        case _:
                                            size.append(len(line_[line_.index(tr1[0][1]):line_.index(j[0]) + 1:]))
                            else:
                                size.append(300)
                        except ValueError:
                            continue
                    if len(size) == 2:
                        min_tr = size.index(min(size))
                        tr2 = [tr2[min_tr]]
                    else:
                        min_tr = size.index(min(size))
                        if min_tr == (0 | 2):
                            line_ = lines[line2]
                        else:
                            line_ = five2
                        tr2 = [tr2[min_tr]]
                # находим массив станций для 1-ой линии
                if line1 == 5:
                    for line in [lines[line1], five2]:
                        try:
                            match line[line.index(station1):line.index(tr1[0][0]) + 1:]:
                                case []:
                                    line = line[line.index(station1):line.index(tr1[0][0]):-1]
                                    line.append(tr1[0][0])
                                case _:
                                    line = line[line.index(station1):line.index(tr1[0][0]) + 1:]
                            # находим массив станций для 2-ой линии
                            match line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]) + 1:]:
                                case []:
                                    line_ = line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]):-1]
                                    line_.append(tr2[0][0])
                                case _:
                                    line_ = line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]) + 1:]
                            # находим массив станций для 3-ой линии
                            line_1 = lines[line3]
                            match line_1[line_1.index(tr2[0][1]):line_1.index(station2) + 1:]:
                                case []:
                                    line_1 = line_1[line_1.index(tr2[0][1]):line_1.index(station2):-1]
                                    line_1.append(station2)
                                case _:
                                    line_1 = line_1[line_1.index(tr2[0][1]):line_1.index(station2) + 1:]
                            line_resault.append(line + line_ + line_1)
                        except ValueError:
                            continue
                if line2 == 5:
                    for line_ in [lines[line2], five2]:
                        try:
                            line = lines[line1]
                            match line[line.index(station1):line.index(tr1[0][0]) + 1:]:
                                case []:
                                    line = line[line.index(station1):line.index(tr1[0][0]):-1]
                                    line.append(tr1[0][0])
                                case _:
                                    line = line[line.index(station1):line.index(tr1[0][0]) + 1:]
                            # находим массив станций для 2-ой линии
                            match line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]) + 1:]:
                                case []:
                                    line_ = line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]):-1]
                                    line_.append(tr2[0][0])
                                case _:
                                    line_ = line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]) + 1:]
                            # находим массив станций для 3-ой линии
                            line_1 = lines[line3]
                            match line_1[line_1.index(tr2[0][1]):line_1.index(station2) + 1:]:
                                case []:
                                    line_1 = line_1[line_1.index(tr2[0][1]):line_1.index(station2):-1]
                                    line_1.append(station2)
                                case _:
                                    line_1 = line_1[line_1.index(tr2[0][1]):line_1.index(station2) + 1:]
                            line_resault.append(line + line_ + line_1)
                        except ValueError:
                            continue
                if line3 == 5:
                    for line_1 in [lines[line3], five2]:
                        try:
                            line = lines[line1]
                            match line[line.index(station1):line.index(tr1[0][0]) + 1:]:
                                case []:
                                    line = line[line.index(station1):line.index(tr1[0][0]):-1]
                                    line.append(tr1[0][0])
                                case _:
                                    line = line[line.index(station1):line.index(tr1[0][0]) + 1:]
                            # находим массив станций для 2-ой линии
                            match line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]) + 1:]:
                                case []:
                                    line_ = line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]):-1]
                                    line_.append(tr2[0][0])
                                case _:
                                    line_ = line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]) + 1:]
                            # находим массив станций для 3-ой линии
                            match line_1[line_1.index(tr2[0][1]):line_1.index(station2) + 1:]:
                                case []:
                                    line_1 = line_1[line_1.index(tr2[0][1]):line_1.index(station2):-1]
                                    line_1.append(station2)
                                case _:
                                    line_1 = line_1[line_1.index(tr2[0][1]):line_1.index(station2) + 1:]
                            line_resault.append(line + line_ + line_1)
                        except ValueError:
                            continue
                else:
                    line = lines[line1]
                    match line[line.index(station1):line.index(tr1[0][0]) + 1:]:
                        case []:
                            line = line[line.index(station1):line.index(tr1[0][0]):-1]
                            line.append(tr1[0][0])
                        case _:
                            line = line[line.index(station1):line.index(tr1[0][0]) + 1:]
                    # находим массив станций для 2-ой линии
                    line_ = lines[line2]
                    match line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]) + 1:]:
                        case []:
                            line_ = line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]):-1]
                            line_.append(tr2[0][0])
                        case _:
                            line_ = line_[line_.index(tr1[0][1]):line_.index(tr2[0][0]) + 1:]
                    # находим массив станций для 3-ой линии
                    line_1 = lines[line3]
                    match line_1[line_1.index(tr2[0][1]):line_1.index(station2) + 1:]:
                        case []:
                            line_1 = line_1[line_1.index(tr2[0][1]):line_1.index(station2):-1]
                            line_1.append(station2)
                        case _:
                            line_1 = line_1[line_1.index(tr2[0][1]):line_1.index(station2) + 1:]
                    line_resault.append(line + line_ + line_1)
            except KeyError:
                continue
    except:
        pass
    # находим все маршруты с тремя пересадками
    try:
        tr1 = []
        tr2 = []
        tr3 = []
        #
        for i in trans[line1].keys():
            try:
                for p in trans[i].keys():
                    try:
                        tr1 = trans[line_fixed_1][i]
                        tr2 = trans[i][p]
                        tr3 = trans[p][line_fixed_2]
                        line2, line3, line4 = i, p, line_fixed_2
                        line = lines[line1]
                        if len(tr1) != 1:
                            size = []
                            for j in tr1:
                                try:
                                    match line[line.index(station1):line.index(j[0]) + 1:]:
                                        case []:
                                            l = line[line.index(station1):line.index(j[0]):-1]
                                            l.append(j[0])
                                            size.append(len(l))
                                        case None:
                                            size.append(1)
                                        case _:
                                            size.append(len(line[line.index(station1):line.index(j[0]) + 1:]))
                                except ValueError:
                                    continue
                            min_tr = size.index(min(size))
                            tr1 = [tr1[min_tr]]
                        else:
                            if tr1[0][0] == tr2[0][1]:
                                continue
                        line_2 = lines[line2]
                        if len(tr2) != 1:
                            size = []
                            for j in tr2:
                                try:
                                    if j[1] != tr1[0][0]:
                                        match line_2[line_2.index(tr1[0][1]):line_2.index(j[0]) + 1:]:
                                            case []:
                                                l = line_2[line_2.index(tr1[0][1]):line_2.index(j[0]) - 1:-1]
                                                l.append(j[0])
                                                size.append(len(l))
                                            case None:
                                                size.append(1)
                                            case _:
                                                size.append(len(line_2[line_2.index(tr1[0][1]):line_2.index(j[0]) + 1:]))
                                    else:
                                        size.append(300)
                                except ValueError:
                                    continue
                            min_tr = size.index(min(size))
                            tr2 = [tr2[min_tr]]
                        line_3 = lines[line3]
                        if len(tr3) != 1:
                            size = []
                            for j in tr3:
                                try:
                                    if j[1] != tr2[0][0]:
                                        match line_3[line_3.index(tr2[0][1]):line_3.index(j[0]) + 1:]:
                                            case []:
                                                l = line_3[line_3.index(tr2[0][1]):line_3.index(j[0]) - 1:-1]
                                                l.append(j[0])
                                                size.append(len(l))
                                            case None:
                                                size.append(1)
                                            case _:
                                                size.append(len(line_3[line_3.index(tr2[0][1]):line_3.index(j[0]) + 1:]))
                                    else:
                                        size.append(100)
                                except ValueError:
                                    continue
                            min_tr = size.index(min(size))
                            tr3 = [tr3[min_tr]]
                        # находим массив станций для 1-ой линии
                        line_1 = lines[line1]
                        match line_1[line_1.index(station1):line_1.index(tr1[0][0]) + 1:]:
                            case []:
                                line_1 = line_1[line_1.index(station1):line_1.index(tr1[0][0]):-1]
                                line_1.append(tr1[0][0])
                            case _:
                                line_1 = line_1[line_1.index(station1):line_1.index(tr1[0][0]) + 1:]
                        # находим массив станций для 2-ой линии
                        line_2 = lines[line2]
                        match line_2[line_2.index(tr1[0][1]):line_2.index(tr2[0][0]) + 1:]:
                            case []:
                                line_2 = line_2[line_2.index(tr1[0][1]):line_2.index(tr2[0][0]):-1]
                                line_2.append(tr2[0][0])
                            case _:
                                line_2 = line_2[line_2.index(tr1[0][1]):line_2.index(tr2[0][0]) + 1:]
                        # находим массив станций для 3-ой линии
                        line_3 = lines[line3]
                        match line_3[line_3.index(tr2[0][1]):line_3.index(tr3[0][0]) + 1:]:
                            case []:
                                line_3 = line_3[line_3.index(tr2[0][1]):line_3.index(tr3[0][0]):-1]
                                line_3.append(tr3[0][0])
                            case _:
                                line_3 = line_3[line_3.index(tr2[0][1]):line_3.index(tr3[0][0]) + 1:]
                        # находим массив станций для 3-ой линии
                        line_4 = lines[line4]
                        match line_4[line_4.index(tr3[0][1]):line_4.index(station2) + 1:]:
                            case []:
                                line_4 = line_4[line_4.index(tr3[0][1]):line_4.index(station2):-1]
                                line_4.append(station2)
                            case _:
                                line_4 = line_4[line_4.index(tr3[0][1]):line_4.index(station2) + 1:]
                        line_resault.append(line_1 + line_2 + line_3 + line_4)
                    except KeyError:
                        continue
            except KeyError:
                continue
    except:
        pass
        # возвращаем наикратчайший маршрут
    return line_resault


if __name__ == '__main__':
    for i in plotting_a_route('Красносельская', 1, 'Алексеевская', 6):
        print(i)
