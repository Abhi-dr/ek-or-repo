from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

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
            
            messages.success(request, "Invalid Credentials")
            return redirect("login")
    
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    
    messages.success(request, "Thanks for using this website!")

    return redirect("login")

def invalid(request):
    return render(request, "invalid.html")


@login_required(login_url="login")
def dashboard(request):
    
    user = request.user
    
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        image = request.FILES["image"]
        
        new_note = Note.objects.create(
            user = user,
            title = title,
            description = desc
        )
        
        new_note.note_img = image
        new_note.save()
        
        messages.success(request, "New note has been added successfully!")
        
        return redirect("notes")
    
    parameters = {
        "user": user
    }
    
    return render(request, "dashboard.html", parameters)
@login_required(login_url="login")
def notes(request):
    
    user = request.user
    notes = Note.objects.filter(user = user)
    
    parameters = {
        "user": user,
        "notes": notes
    }
    
    return render(request, "notes.html", parameters)

@login_required(login_url="login")
def edit_note(request, id):
    
    note = Note.objects.get(id = id)
    
    if request.method == "POST":
        new_title = request.POST.get("title")
        new_description = request.POST.get("description")
        
        note.title = new_title
        note.description = new_description
        
        note.save()
        messages.info(request, "Note has been UPDATED successfully!")

        
        return redirect("notes")
    
    parameters = {
        "note": note
    }
    
    return render(request, "edit_note.html", parameters)

@login_required(login_url="login")
def delete_note(request, id):
    
    note = Note.objects.get(id = id)
    note.delete()
    
    messages.success(request, "Note has been deleted successfully!")
    
    return redirect("notes")

# =================================================================

def page_not_found_view(request, exception):
    return render(request, "404.html", status=404, parameters = {"exception": exception})