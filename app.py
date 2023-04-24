from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def signup():
    return render_template('index.html')
@app.route('/register/')
def register():
    return render_template('map_test.htm')
@app.route('/signin/')
def signin():
    return render_template('login.html')

if __name__ == "__main__":
  app.run(debug=True)