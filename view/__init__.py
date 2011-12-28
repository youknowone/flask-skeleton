
from template import app
import flask

@app.route('/')
def index():
    return flask.redirect(flask.url_for('plain', page='index'))

@app.route('/<page>')
def plain(page):
    return flask.render_template(page + '.html')

@app.route('/static/<filename>')
def static(filename):
    return app.send_static_file(filename)

@app.errorhandler(404)
def error404(e):
    return '<h2>404 Not Found</h2>'
