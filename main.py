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
    if request.method == 'POST':
        input_1 = request.form['input_1']
        input_2 = request.form['input_2']

        print(input_1, input_2)
        # маршрут
        if input_1 == '' and input_2 == '':
            route_ = []
        else:
            route_ = [input_1, input_2]

        # цвет точки у input1

        if input_1 in red:
            point_color = 'red'
        else:
            point_color = ''
        # цвет точки у input2
        if input_2 in red:
            point_color2 = 'red'
        else:
            point_color2 = ''

        # HTML код

        return render_template('index.html', v1=input_1, v2=input_2,
                               point_color=point_color, point_color2=point_color2,
                               route_=route_)
    if request.method == 'GET':
        return render_template('index.html', route_=route_)


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(debug=True)

