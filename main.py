from flask import Flask, json, request, render_template, url_for
import postgreSQL
import logging
from datetime import date

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)


########################
#  ДОДЕЛАТЬ ПОЛЕ ДАТЫ  #
########################
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['title']
        email = request.form['email']
        text = request.form['Comment-text']

        postgreSQL.create_comment(name, email, text, date.today())

    comments = postgreSQL.select_comments()

    return render_template("index.html", comments=comments)


if __name__ == '__main__':
    app.run(debug=True)
