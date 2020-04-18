import flask
import flask_bootstrap

app = flask.Flask(__name__)
bootstrap = flask_bootstrap.Bootstrap(app)

@app.route('/')
def index():
    return flask.render_template('index.html') # render_template是指轉譯後面的html template，其整合了Jinja2模板引擎與app
# Jinja2可以辨識任何型態的變數，如python list, dictionary, object...

@app.route('/user/<name>')
def user(name):
    return flask.render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return flask.render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8050') 