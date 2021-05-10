from flask import Flask, render_template

app = Flask(__name__)


@app.route('/play')
def level1():
    return render_template("index.html", num_square=3,color ="blue")


@app.route('/play/<num>')
def level2(num):
    return render_template('index.html', num_square=int(num),color ="blue")

@app.route('/play/<num>/<color>')
def level3(num,color):
    return render_template('index.html', num_square=int(num), color=color)




if __name__=="__main__":
    app.run(debug=True)
