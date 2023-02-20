from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/calculate')
def number():
    number = request.args.get('number')

    if number.isnumeric():
        is_even = int(number) % 2 == 0
        is_error = not number
        return render_template('calculate.html', number=number, is_even=is_even)
    else:
        return render_template('calculate.html', number=number)


if __name__ == '__main__':
    app.run(debug=True)
