from flask import Flask, render_template, url_for, request
import sqlite3

app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        con=sqlite3.connect('user1.db')
        c=con.cursor()

        name=request.form['name']
        email=request.form['email']
        password=request.form['password']

        print(name,email,password)

        query="SELECT name,email,password FROM users where name='"+name+"' and email='"+email+"' and password='"+password+"'"
        c.execute(query)

        results=c.fetchall()

        if len(results) == 0:
            print("Sorry incorrect credentials")
        else:
            return render_template('pre.html')
    return render_template('login _1.html')
# @app.route('/')
# def home():
#     return render_template('loading.html')
@app.route('/register/')
def register():
    return render_template('login.html')
@app.route('/signin/')
def signin():
    return render_template('index.html')
    




if __name__ == "__main__":
  app.run(debug=True)
