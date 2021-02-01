from flask import Flask , render_template
import os

app = Flask('url for function')

@app.route('/')
def index():
    prefix = 'static/'
    images = [os.path.join(prefix,p) for p in os.listdir('d://prince//programming/web development/backend by Flask//static') if str(p).endswith('.jpg')]
    #1.{{url_for("name of the function")}}
    #2/ {{url_for('static',filename='name of the static file')}}

    return render_template('index.html',images = images)


@app.route('/unhome')
def index2():
    return render_template('index2.html')


if __name__ == '__main__':
    app.run(debug=True)