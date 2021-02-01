from flask import Flask, render_template
import time

app = Flask("jinja template varible")

@app.route("/")
def index():
    name = 'PRIYANSHU'    
    lst_names = [name,'devendra','dolly']
    data_set = {
        'Framework':'flask',
        'class':'jinja'
    }
    
    return render_template("index.html",name=name ,lst_names = lst_names,data=data_set,time=time.asctime())


if __name__ == '__main__':
    app.run(debug=True)    