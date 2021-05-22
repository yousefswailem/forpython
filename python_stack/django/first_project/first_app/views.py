from django.shortcuts import render , redirect

# Create your views here.
def main(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1

    return render(request, "index.html")

def add2(request):
    request.session['counter'] +=1

    return redirect('/')

def destroy(request):
    del request.session['counter']

    return redirect('/')

