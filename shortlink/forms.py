from django import forms


class URLForm(forms.Form):
    long_url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Введите ссылку для сокращения'}))
