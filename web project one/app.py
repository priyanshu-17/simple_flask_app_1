from flask import *



app = Flask('me myself and I')



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/list')
def lists():       
    return render_template('list.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/tq')
def tq():
    name = request.args.get('name')
    name_contact = request.args.get('name_contact')
    return render_template('tq.html',name=name,name_contact=name_contact)


if __name__ == '__main__':
    app.run(debug=True)
