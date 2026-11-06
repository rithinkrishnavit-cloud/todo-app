from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Todo

# Create your views here.


# User register
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "todo/register.html", {"form": form})


# User login
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "todo/login.html", {"form": form})


# User logout
def user_logout(request):
    logout(request)
    return redirect("user_login")


# home page / show todos
@login_required
def home(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, "todo/home.html", {"todos": todos})


# add task
@login_required
def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description", "")
        Todo.objects.create(user=request.user, title=title, description=description)

        return redirect("home")
    return render(request, "todo/add_todo.html")


# complete task
@login_required
def complete_todo(request, id):

    todo = get_object_or_404(Todo, id=id, user=request.user)

    if request.method == "POST":
        todo.completed = True
        todo.save()
    return redirect("home")


# task delete
@login_required
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == "POST":
        todo.delete()
    return redirect("home")


# task update
def update_todo(request, id):

    todo = get_object_or_404(Todo, id=id, user=request.user)

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        todo.title = title
        todo.description = description

        todo.save()
        return redirect("home")

    return render(request, "todo/update_todo.html", {"todo": todo})
