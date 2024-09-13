from django import forms


class NameForm(forms.Form):
    name = forms.CharField(label='--Введите  логин:', max_length=30)
    passw = forms.CharField(label='--Введите пароль min.8зн.:', min_length=8)
    passw1 = forms.CharField(label='--Подтвердите пароль:', min_length=8)
    age = forms.CharField(label='--Введите возраст:', max_length=3)


