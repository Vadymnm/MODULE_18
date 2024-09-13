from django.http import HttpResponse
from django.shortcuts import render
from .forms import NameForm

users = ['Vasya', 'Petya', 'Kolya']

# **** === Django === ********************************************************************

def reg_page_django(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            passw = form.cleaned_data['passw']
            passw1 = form.cleaned_data['passw1']
            age = form.cleaned_data['age']

            info = {"name": name, "passw": passw, "age": age}
            print(info)
        # redirect to a new URL:
            if name in users:
                return HttpResponse("/!!! Пользователь уже существует !!!/")
            if passw != passw1:
                return HttpResponse("/!!! Пароли не совпадают !!!/")
            if int(age) < 18:
                return HttpResponse("/!!! Вы должны быть старше 18 !!!/")
            return HttpResponse({"Приветствуем,", name})

        return render(request, 'reg_django.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, "reg_django.html", {"form": form})

#  ***** === HTML ==== **********************************************************

def reg_page_html(request):
    if request.method == "POST":
        name = request.POST.get('name')
        passw = request.POST.get('passw')
        passw1 = request.POST.get('passw1')
        age = request.POST.get('age')

        # print(f"name: {name}")
        # print(f"passw: {passw}")
        # print(f"passw1: {passw1}")
        # print(f"age: {age}")

        info = {"name": name, "passw": passw, "age": age}
        print(info)

        # redirect to a new URL:
        if name in users:
            return HttpResponse("/!!! Пользователь уже существует !!!/")
        if passw != passw1:
            return HttpResponse("/!!! Пароли не совпадают !!!/")
        if int(age) < 18:
            return HttpResponse("/!!! Вы должны быть старше 18 !!!/")
        return HttpResponse({"Приветствуем,", name})

    return render(request, 'registration_page.html')
# ************************************************************************
