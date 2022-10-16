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


@app.route("/", methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        input_1 = request.form['input1']
        input_2 = request.form['input2']

        if input_1 == '':
            button_input_1 = 'display:none'
        else:
            button_input_1 = ''
        if input_2 == '':
            button_input_2 = 'display:none'
        else:
            button_input_2 = ''

        if input_1 in red:
            point_color = 'red'
        else:
            point_color = ''

        # ---------------------------
        if input_2 in red:
            point_color2 = 'red'
        else:
            point_color2 = ''

        return render_template('index.html', v1=input_1, v2=input_2,
                               button_input_1=button_input_1, button_input_2=button_input_2,
                               point_color=point_color, point_color2=point_color2)


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(debug=True)

