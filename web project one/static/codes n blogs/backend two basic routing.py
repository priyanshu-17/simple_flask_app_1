from flask import Flask
import time 

application = Flask('multiple paging via routing')

@application.route('/')
def function1():
    t = time.asctime()
    return f'<h1>welcome!!!</h1> <a style="font-size:22px;font-family:monospace;"href="/page2">click_for the next page</a> <h2 style="background-color:green;">your were here at {t} </h2>'

@application.route('/page2')
def function2():
    t = time.asctime()

    return f'<h1>welcome this is 2nd page!!!</h1> <a style="font-size:22px;font-family:monospace;"href="/">click_for the previous page</a> <h2 style="background-color:green;">your were here at {t} </h2>'


if __name__ == "__main__":
    application.run(debug=True)


