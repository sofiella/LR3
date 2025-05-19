from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def convert():
    rates = {
        "rur": {"rur": 1, "usd": 0.0124, "eur": 0.0109},
        "usd": {"rur": 80.9644, "usd": 1, "eur": 0.8808},
        "eur": {"rur": 91.9169, "usd": 1.1353, "eur": 1}
    }

    _from = request.form.get('from')
    _to = request.form.get('to')
    try:
        amount = float(request.form.get('amount'))
    except ValueError:
        return render_template('index.html', ans="Ошибка: введите число.")

    result = round(amount * rates[_from][_to], 2)
    return render_template('index.html', ans=f"{amount} {_from.upper()} = {result} {_to.upper()}")


if __name__ == '__main__':
    app.run(debug=True)
