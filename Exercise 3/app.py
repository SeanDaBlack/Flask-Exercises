from flask import Flask, render_template, request


app = Flask(__name__)


students = {}


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        students.update(
            {request.form.get('name'): request.form.get('organization')})

    return render_template('register.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)
