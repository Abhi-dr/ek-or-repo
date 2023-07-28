from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from .models import Note

def login(request):
    
    if request.method == "POST":
        uname = request.POST.get("username")
        pword = request.POST.get("password")
        
        user = auth.authenticate(username = uname, password = pword)
        
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
    
        else:
            return redirect("invalid")
    
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect("login")

def invalid(request):
    return render(request, "invalid.html")

def dashboard(request):
    
    user = request.user
    
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        
        new_note = Note.objects.create(
            user = user,
            title = title,
            description = desc
        )
        
        new_note.save()
        return redirect("notes")
    

    
    
    
    
    parameters = {
        "user": user
    }
    
    return render(request, "dashboard.html", parameters)

def notes(request):
    
    user = request.user
    notes = Note.objects.filter(user = user)
    
    parameters = {
        "user": user,
        "notes": notes
    }
    
    return render(request, "notes.html", parameters)

def edit_note(request, id):
    
    note = Note.objects.get(id = id)
    
    if request.method == "POST":
        new_title = request.POST.get("title")
        new_description = request.POST.get("description")
        
        note.title = new_title
        note.description = new_description
        
        note.save()
        
        return redirect("notes")
    
    parameters = {
        "note": note
    }
    
    return render(request, "edit_note.html", parameters)

def delete_note(request, id):
    
    note = Note.objects.get(id = id)
    note.delete()
    
    return redirect("notes")