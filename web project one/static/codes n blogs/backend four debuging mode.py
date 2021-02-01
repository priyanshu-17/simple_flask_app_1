from flask import Flask



site = Flask("debugging mode")

@site.route('/')
def login_First():
    return f"<h1>NAME: <input type='text' ></h1> <h1>CLASS: <input type='text' ></h1>"


@site.route('/login/<user_name>')
def logined(user_name):
    import random
    lst = [str(user_name),str(random.randint(1000,9999))]
    return f"<h1 style='font-family:monospace;'>hello user from now on your username will be: - {'.'.join(lst)} </h1>".upper()


@site.route("/drive/<age>")
def driving(age):
    age = int(age)

    
    try:    
        if age <18 or age > 60:
            raise ValueError('your age is not accepted')
    
        return f'<h1>your age is {age} you can drive</h1>'
    except Exception as ValueError:
        if age <18:
            return f"<h1>you have to wait kiddo untill you reach 18</h1>"
        elif age > 60:
            return f"<h1>your age of driving a hot cars are now over grands heir a driver </h1>"


if __name__ == "__main__":
    site.run(debug=True) #note that use debug mode only when in development not during deployement