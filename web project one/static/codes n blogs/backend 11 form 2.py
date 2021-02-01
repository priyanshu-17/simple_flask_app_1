from flask import Flask,render_template
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField,IntegerField


app = Flask('form 2')

app.config['SECRET_KEY'] = 'p2i0r0y4'


class forms(FlaskForm):
    name = StringField('what is your name ??')
    age = IntegerField('what is your age ??')
    submit = SubmitField('submit')


@app.route('/', methods=['GET','POST'])
def index():
    name = False
    age = False
    frm = forms()
    if frm.validate_on_submit():
        name = frm.name.data
        age = frm.age.data
        frm.name.data = ''
        frm.age.data = ''
    return render_template('page one.html',frm=frm, name = name,age=age)


if __name__ == '__main__':
    app.run(debug=True)


