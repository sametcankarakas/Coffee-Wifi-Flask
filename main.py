from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donxc<zWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url = URLField(label='Cafe Location on Google Maps(URL)', validators=[URL(message='Invalid URL')])
    opening = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing = StringField('Closin Time e.g. 5PM', validators=[DataRequired()])
    coffee = SelectField(u'Coffee Rating', choices=[('✘'), ('☕'), ('☕☕'), ('☕☕☕'), ('☕☕☕☕'), ('☕☕☕☕☕')])
    wifi = SelectField(u'Wifi Strength Rating', choices=[('✘'), ('💪'), ('💪💪'), ('💪💪💪'), ('💪💪💪💪'), ('💪💪💪💪💪')])
    power = SelectField(u'Power Socket Availability', choices=[('✘'), ('🔌'), ('🔌🔌'), ('🔌🔌🔌'), ('🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌')])
    submit = SubmitField(label='Submit')




# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    coffee_form_add=[]
    coffee_form_add.append(form.cafe.data)
    coffee_form_add.append(form.url.data)
    coffee_form_add.append(form.opening.data)
    coffee_form_add.append(form.closing.data)
    coffee_form_add.append(form.coffee.data)
    coffee_form_add.append(form.wifi.data)
    coffee_form_add.append(form.power.data)
    print(coffee_form_add)
    # cafe_name = form.cafe.data
    # url_link = form.url.data
    # opening_time = form.opening.data
    # closing_time = form.closing.data
    # coffee_quality = form.coffee.data
    # wifi_quality = form.wifi.data
    # power_quantity = form.power.data
    # coffee_shop_add = []
    if form.validate_on_submit():
        print("True")
        with open("cafe-data.csv", "a", encoding='utf-8') as fp:
            wr = csv.writer(fp, lineterminator='\n')
            wr.writerow(coffee_form_add)
        return render_template('index.html', form=form)

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', encoding="utf-8", newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        counter = 0
        for row in csv_data:
            counter += 1
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows, counter=counter)


if __name__ == '__main__':
    app.run(debug=True)
