from flask import Flask, render_template, request, redirect
app = Flask(__name__)


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

        return render_template('index.html', v1=input_1, v2=input_2,
                               button_input_1=button_input_1, button_input_2=button_input_2)


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(debug=True)

