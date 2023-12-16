from django.shortcuts import render, redirect
from . models import User
from . forms import UserForm


def show_users(request):
    users = User.objects.all()

    return render(request, 'show_users.html', {'users': users})


def create_users(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("list of users")

    return render(request, 'create_users.html', {"form": form})


def delete_users(request, pk):
    user_to_delete = User.object.get(pk=pk)
    user_to_delete.delete()
