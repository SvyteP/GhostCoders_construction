
from django import forms

class InputForm(forms.Form):
    user_input = forms.CharField(label='Enter a value', max_length=100)


class TitleForm(forms.Form):
    input_title = forms.CharField(label='Введите название', max_length=100)
