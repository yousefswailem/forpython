from django import django, render_template, request, redirect, session

def count():
    request.session['counter']=0
    return redirect("/count")

def add_counter():
    count=request.session["counter"]
    count=count+1
    request.session["counter"]=count
    return render_template("counter.html",count=request.session['counter'])

def clear():
    request.session.clear()
    return redirect('/')

def add():
    request.session['counter']+=2
    return render_template("counter.html",count=request.session['counter'])

def add2():
    request.post['number']
    request.session['counter']+= int(request.post['number'])
    request.session['theadd']=request.post['number']

    return redirect('/')

