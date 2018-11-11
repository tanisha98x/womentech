from flask import Flask, render_template, redirect, flash, request, url_for
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

DEGREE = [('1', "Middle School"), ('2', "High School"), ('3', "College Student"), ('4', "Grad School")]

class MatchForm(Form):
    name = StringField('Name', [validators.optional(), validators.length(max=200)])
    email = StringField('Email Address', [validators.optional(), validators.length(max=200)])
    degree = SelectField(label='Degee', choices=DEGREE)
    skills = StringField('Skills', [validators.optional(), validators.length(max=200)])
    otherinterests = StringField('Other Interests', [validators.optional(), validators.length(max=200)])


@app.route('/fit', methods=['GET', 'POST'])
def fit():
    form = MatchForm(request.form)
    if request.method == 'POST':
        name = form.name.data
        email = form.email.data
        degree = form.degree.data
        skills = form.skills.data
        otherinterests = form.otherinterests.data
        jsonFile = convertJson(name, email, degree, skills, otherinterests)
        companies = "Amazon"

        return render_template('displayresult.html', companies = companies)

    return render_template('fit.html', form=form)

def convertJson(name, email, degree, skills, otherinterests):
    result = []
    myjson = {
            'Name': name,
            'Email': email,
            'Degree': degree,
            'Skills': skills,
            'Interests': otherinterests
    }
    result.append(myjson)
    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True)
