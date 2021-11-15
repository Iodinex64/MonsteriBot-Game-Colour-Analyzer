from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/fighting')
def fighting():
    return render_template("fighting.html")


@app.route('/moba')
def moba():
    return render_template("moba.html")


@app.route('/platforming')
def platforming():
    return render_template("platforming.html")


@app.route('/racing')
def racing():
    return render_template("racing.html")


@app.route('/rpg')
def rpg():
    return render_template("rpg.html")


@app.route('/shooter')
def shooter():
    return render_template("shooter.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
