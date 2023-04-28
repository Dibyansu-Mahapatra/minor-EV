from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('loading.html')
@app.route('/register/')
def register():
    return render_template('login.html')
@app.route('/signin/')
def signin():
    return render_template('battery.html')
    

if __name__ == "__main__":
  app.run(debug=True)