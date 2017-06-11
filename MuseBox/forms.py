from django import forms


class SelectionChansons(forms.Form):
    TitreChanson1 = forms.CharField(label='Title of the song #1', max_length=100)
    TitreChanson2 = forms.CharField(label='Title of the song #2', max_length=100)
    TitreChanson3 = forms.CharField(label='Title of the song #3', max_length=100)