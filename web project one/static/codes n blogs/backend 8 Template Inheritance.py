from flask import Flask , render_template


app = Flask("TEMPLATE INHERITANCE")


@app.route('/')
def index():
    return render_template('nav.html')

@app.route('/about')
def about():
    return render_template('content.html')

@app.route('/time')
def time():
    import time
    return render_template('add friend.html',t = time.asctime())


if __name__ == "__main__":
    app.run(debug=True)