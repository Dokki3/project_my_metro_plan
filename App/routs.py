from flask import render_template, request

from App import app
from function import plotting_a_route
from func_time import determining_the_time
from data import lines


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key


@app.route("/", methods=['POST', 'GET'])
def main():
    line1 = 0
    line2 = 0
    route_ = []
    point_color = '#ccc'
    point_color2 = '#ccc'
    if request.method == 'POST':
        input_1 = request.form['input_1']
        input_2 = request.form['input_2']
        all_station = [i[1] for i in list(lines.items())]

        # цвет точки у input1
        point_color = request.form['p1']
        point_color2 = request.form['p2']

        # время поездки
        time = 0

        point_colors = [point_color, point_color2]

        # узнаём номер линии
        match point_colors:
            case ['#da2128', _]:
                line1 = 1
            case ['#48b85e', _]:
                line1 = 2
            case ['#0078bf', _]:
                line1 = 3
            case ['#00c1f3', _]:
                line1 = 4
            case ['#00c1f4', _]:
                line1 = '4A'
            case ['#894e35', _]:
                line1 = 5
            case ['#f58220', _]:
                line1 = 6
            case ['#8e479b', _]:
                line1 = 7
            case ['#ffc61a', _]:
                line1 = 8
            case ['#ffc61b', _]:
                line1 = '8A'
            case ['#a1a2a3', _]:
                line1 = 9
            case ['#b4d445', _]:
                line1 = 10
            case ['#6ac9c8', _]:
                line1 = 11
            case ['#6ac9c9', _]:
                line1 = '11A'
            case ['#acbfe3', _]:
                line1 = 12
            case ['#e66ac0', _]:
                line1 = 15

        match point_colors:
            case [_, '#da2128']:
                line2 = 1
            case [_, '#48b85e']:
                line2 = 2
            case [_, '#0078bf']:
                line2 = 3
            case [_, '#00c1f3']:
                line2 = 4
            case [_, '#00c1f4']:
                line2 = '4A'
            case [_, '#894e35']:
                line2 = 5
            case [_, '#f58220']:
                line2 = 6
            case [_, '#8e479b']:
                line2 = 7
            case [_, '#ffc61a']:
                line2 = 8
            case [_, '#ffc61b']:
                line2 = '8A'
            case [_, '#a1a2a3']:
                line2 = 9
            case [_, '#b4d445']:
                line2 = 10
            case [_, '#6ac9c8']:
                line2 = 11
            case [_, '#6ac9c9']:
                line2 = '11A'
            case [_, '#acbfe3']:
                line2 = 12
            case [_, '#e66ac0']:
                line2 = 15

        # маршрут
        route_ = []
        if input_1 == '' or input_2 == '':
            route_ = []
        else:
            station1 = input_1
            station2 = input_2
            match input_1:
                case ('Проспект Вернадского' | 'Парк культуры' | 'Комсомольская' | 'Белорусская' | 'Павелецкая'
                | 'Кунцевская' | 'Парк Победы' | 'Киевская' | 'Смоленская' | 'Арбатская' | 'Курская'
                | 'Электрозаводская' | 'Проспект Мира' | 'Октябрьская' | 'Таганская' | 'Китай-город' | 'Третьяковская'
                | 'Авиамоторная' | 'Мичуринский проспект' | 'Петровско-Разумовская' | 'Савёловская' | 'Деловой центр'):
                    station1 += str(line1)

            match input_2:
                case ('Проспект Вернадского' | 'Парк культуры' | 'Комсомольская' | 'Белорусская' | 'Павелецкая'
                | 'Кунцевская' | 'Парк Победы' | 'Киевская' | 'Смоленская' | 'Арбатская' | 'Курская'
                | 'Электрозаводская' | 'Проспект Мира' | 'Октябрьская' | 'Таганская' | 'Китай-город' | 'Третьяковская'
                | 'Авиамоторная' | 'Мичуринский проспект' | 'Петровско-Разумовская' | 'Савёловская' | 'Деловой центр'):
                    station2 += str(line2)

            for i in all_station:
                if station1 in i:
                    if line1 == 0:
                        line1 = get_key(i, lines)
                    break
            else:
                return render_template('index.html', route_=route_, point_color=point_color, point_color2=point_color2)

            for i in all_station:
                if station2 in i:
                    if line2 == 0:
                        line2 = get_key(i, lines)
                    break
            else:
                return render_template('index.html', route_=route_, point_color=point_color, point_color2=point_color2)

            route_ = plotting_a_route(station1, line1, station2, line2)
            route_.sort(key=determining_the_time)
            for i in route_:
                print(i, determining_the_time(i))
            route_ = route_[0]
            # узнаём время поездки
            try:
                time = determining_the_time(route_)
                match line1:
                    case 1 | 2 | 3 | 5 | 6 | 7 | 8 | '8A' | 9 | 10 | 11 | '11A':
                        time += 2
                    case 4 | '4A' | 12 | 15:
                        time += 4
                if time < 60:
                    time = f'{determining_the_time(route_)} минут'
                else:
                    time = f'{time // 60} час {time % 60} минут'
            except TypeError:
                pass

        # кнопки сброса
        if input_1 == '':
            bi1 = 'display: none;'
        else:
            bi1 = ''
        if input_2 == '':
            bi2 = 'display: none;'
        else:
            bi2 = ''

        # HTML код

        return render_template('index.html', v1=input_1, v2=input_2, bi1=bi1, bi2=bi2,
                               point_color=point_color, point_color2=point_color2,
                               route_=route_, time=time)
    if request.method == 'GET':
        return render_template('index.html', route_=route_, point_color=point_color, point_color2=point_color2)
