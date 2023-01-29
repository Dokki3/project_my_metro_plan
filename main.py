from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# variables
red = ['Бульвар Рокоссовского', 'Черкизовская', 'Преображенская площадь', 'Сокольники',
       'Красносельская', 'Комсомольская', 'Красные Ворота', 'Чистые пруды',
       'Лубянка', 'Охотный Ряд', 'Библиотека имени Ленина', 'Кропоткинская',
       'Парк культуры', 'Фрунзенская', 'Спортивная', 'Воробьёвы горы',
       'Университет', 'Проспект Вернадского', 'Юго-Западная', 'Тропарёво',
       'Румянцево', 'Саларьево', 'Филатов Луг', 'Прокшино',
       'Ольховая', 'Коммунарка', ]

green = ['', ]


@app.route("/", methods=['POST', 'GET'])
def main():
    route_ = []
    point_color = '#ccc'
    point_color2 = '#ccc'
    if request.method == 'POST':
        input_1 = request.form['input_1']
        input_2 = request.form['input_2']

        # маршрут
        if input_1 == '' or input_2 == '':
            route_ = []
        else:
            route_ = [input_1, input_2]

        # цвет точки у input1
        point_color = request.form['p1']
        point_color2 = request.form['p2']

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
                               route_=route_)
    if request.method == 'GET':
        return render_template('index.html', route_=route_, point_color=point_color, point_color2=point_color2)


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(debug=True)

