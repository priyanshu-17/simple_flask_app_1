from flask import Flask , render_template
import time
import os


app = Flask("TEMPLATE CONTROL FLOW")

@app.route("/")
def index2():
    # photo = '/static/final one.jpg'
    
    data = {
        "NAME":"ID",
        'priyanshu':'priyanshu24003@ybl',
        'himanshu':'123',
        'arpit':'5222',
        'sonu':'2002',
        'json':'java script object notation',
        'date':time.strftime('%d/%m/%y'),
        'time':time.strftime('%H:%M:%S')

    }

    return render_template('index2.html',data=data)
    


if __name__ == '__main__':
    app.run(debug=True)    
