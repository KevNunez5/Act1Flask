from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from wtforms.fields import DecimalField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Nuevo formulario para multiplicar un número
class MultiplyForm(FlaskForm):
    number = DecimalField('Enter a number to multiply by 2:', validators=[DataRequired()])
    submit = SubmitField('Multiply')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# Nueva ruta para multiplicar un número
@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    result = None
    form = MultiplyForm()
    if form.validate_on_submit():
        number = form.number.data
        result = number * 2
    return render_template('multiply.html', form=form, result=result)


if __name__ == '__main__':
    app.run(debug=True)
