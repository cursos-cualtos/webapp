from flask import Flask, render_template
from data import db

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/team/listing')
def team_listing():
    return render_template('team_listing.html', team=db)

if __name__ == "__main__":
    app.run(port=5000)