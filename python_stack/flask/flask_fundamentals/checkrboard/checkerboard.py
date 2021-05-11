from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')

def levle1():
    return render_template('index.html',num_row=4,num_col=4)

@app.route('/<num>')

def levle2(num):
    return render_template('index.html',num_row=2, num_col=4)

@app.route('/<num1>/<num2>')

def levle3(num1,num2):
    return render_template('index.html',num_row=int(num1), num_col=int(num2))
if __name__=="__main__":
    app.run(debug=True)