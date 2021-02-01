from flask import Flask , render_template , request



application = Flask(__name__)


@application.route("/")
def home():
    return render_template('base.html')


@application.route('/form')
def form():
    return render_template('form.html')

@application.route('/tq')
def tq():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('tq.html',first=first)

@application.route('/page')
def page():
    return render_template('page.html')


if __name__ == '__main__':
    application.run(debug=True)