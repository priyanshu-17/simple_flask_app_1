from flask import Flask
import random

app = Flask(__name__)


@app.route('/') #routing is like creatin a page or an adresss and yes it is a decorator
def greet():
    name = 'Priyanshu'
    lst = ['red','cyan','purple','orange','yellow','green']

    return f"<body style='background-color:black;'><h1 style='color:{random.choice(lst)};'>{name} !!!</h1> <h2 style='color:{random.choice(lst)};'>{name} !!!</h2> <h3 style='color:{random.choice(lst)};'>{name} !!!</h3> <h4 style='color:{random.choice(lst)};'>{name} !!!</h4> <h5 style='color:{random.choice(lst)};'>{name} !!!</h5> <h6 style='color:{random.choice(lst)};'>{name} !!!</h6></body>"


if __name__ == '__main__':
    app.run(debug=True)

