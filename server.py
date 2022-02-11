from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play/<int:num>')
def playnum(num):
    return render_template('playbox.html', num=num)

@app.route('/play/<int:num>/<string:color>')
def playnum_and_color(num, color):
    return render_template('playnum_and_color.html', num = num, color=color)

if __name__ =="__main__":
    app.run(debug=True)