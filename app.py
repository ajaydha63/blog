from flask import Flask, render_template, url_for
from forms import RegistrationForms, LoginForms
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f42f73ed6d2738e0e4650c03b92af1d6'

posts = [
    {
        'author': 'Kabibi',
        'title': 'Who is the best QB in the NFL right now?',
        'content': 'Ive been wondering who the best Qb is for a while becasue i want to know who to get in fantasy football but i just cant figure it out.',
        'date_posted': 'october 6th, 2021'
    },
    {
        'author': 'Denius',
        'title': ' Response to - Who is the best QB in the NFL right now?',
        'content': 'If I were you I would take Kyler Murray he is a dual threat and front runner for MVP and a great pickup.',
        'date_posted': 'october 7th, 2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')



if __name__ == '__main__':
    app.run(debug=True)
