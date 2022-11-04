from flask import Flask
from healthcheck import HealthCheck
from add_one import add_one

health = HealthCheck()

app = Flask(__name__)


@app.route('/add_one')
def add():
    return f'<h1>{str(add_one(1))}</h1>'


@app.route('/')
def home():
    return '<h1>Hi! This is on OpenShift.</h1>'


app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
