from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('base.html', **param)


@app.route('/training/<prof>')
def training_prof(prof):
    param = {}
    param['prof'] = prof
    param['img1'] = f"{url_for('static', filename='img/1.png')}"
    param['img2'] = f"{url_for('static', filename='img/2.png')}"
    return render_template('base.html', **param)


@app.route('/list_prof/<list>')
def list_prof(list):
    param = {}
    param['list'] = list
    return render_template('index.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
