from django import forms


class UserSongs(forms.Form):
    songTitle1 = forms.CharField(label='Title of the song #1', max_length=100)
    songTitle2 = forms.CharField(label='Title of the song #2', max_length=100)
    songTitle3 = forms.CharField(label='Title of the song #3', max_length=100)