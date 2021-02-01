from flask import Flask

web = Flask('dynamic routing or argument passing into a page')

@web.route('/')
def greet():
    return "<h1>hello User !!</h2>"


@web.route('/user/<username>') #using/<argument> to pass argument in the assosiated function
def hello_user(username): #using argument to give data in the function
    import random
    clr = ['blue','cyan','red','yellow','pink','green']
    return f'<h2>hello my dear user <span style="font-size:40px;font-family:monospace; color:{random.choice(clr)};">{username.upper()}</span> </h2>'



if __name__ == '__main__':
    web.run(debug=True)