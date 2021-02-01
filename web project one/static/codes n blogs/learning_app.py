from flask import Flask
import random

app = Flask(__name__)


@app.route('/') #routing is like creatin a page or an adresss and yes it is a decorator
def greet():
    name = 'Priyanshu'
    lst = ['red','cyan','purple','orange','yellow','green']

    return f"<body style='background-color:black;'><h1 style='color:{random.choice(lst)};'>{name} !!!</h1> <h2 style='color:{random.choice(lst)};'>{name} !!!</h2> <h3 style='color:{random.choice(lst)};'>{name} !!!</h3> <h4 style='color:{random.choice(lst)};'>{name} !!!</h4> <h5 style='color:{random.choice(lst)};'>{name} !!!</h5> <h6 style='color:{random.choice(lst)};'>{name} !!!</h6></body>"

import time 


@app.route('/page2')
def function2():
    t = time.asctime()

    return f'<h1>welcome this is 2nd page!!!</h1> <a style="font-size:22px;font-family:monospace;"href="/">click_for the previous page</a> <h2 style="background-color:green;">your were here at {t} </h2>'

@app.route('/user/<username>') #using/<argument> to pass argument in the assosiated function
def hello_user(username): #using argument to give data in the function
    import random
    clr = ['blue','cyan','red','yellow','pink','green']
    return f'<h2>hello my dear user <span style="font-size:40px;font-family:monospace; color:{random.choice(clr)};">{username.upper()}</span> </h2>'



if __name__ == '__main__':
    app.run(debug=True)