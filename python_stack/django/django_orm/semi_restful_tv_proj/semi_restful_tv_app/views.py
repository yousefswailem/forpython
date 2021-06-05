# from django.http.response import 
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from .models import Show

# Create your views here.

def show_all(request):
    #shows all the shows in /shows

    context = {
        'shows': Show.objects.all()
    }

    return render(request, 'all_shows.html', context)

def add_form(request):
    # show a form to add a show to db
    return render(request, 'add_show.html')

def add(request):
    # shows/add
    #create a new show and add it to database
    
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/new')

        
    if request.method == 'POST' :
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        desc = request.POST['desc']

        Show.objects.create(title=title, network=network, release_date=release_date,desc=desc)
        id = Show.objects.last().id

    return redirect(f'/shows/{id}')


def edit(request, id):
    # shows/<int:id>/edit
    context = {
        'id': id
    }

    return render(request,'edit_show.html', context)
    

def update(request, id):

    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{id}/edit')
    
        

    #update a selected show (selected by id)
    elif request.method == 'POST' :
        show_to_be_updated = Show.objects.get(id=id)
        show_to_be_updated.title = request.POST['title']
        show_to_be_updated.network = request.POST['network']
        show_to_be_updated.release_date = request.POST['release_date']
        show_to_be_updated.desc = request.POST['desc']
        messages.success(request, "Show successfully updated")
        show_to_be_updated.save()
        
        return redirect(f'/shows/{id}')

        
def show_one (request, id):
    # /shows/<int:id>
    # shows just a single shows with its detailes 
    show = Show.objects.get(id=id)
    context = {
        'id': id,
        'title': show.title,
        'network':show.network,
        'release_date':show.release_date,
        'desc':show.desc,
        'updated_at':show.updated_at
    }

    return render(request,'single_show_details.html', context)
    
def delete(request, id):
    # /shows/<int:id>/delete
    # deletes a specified show from the database
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')