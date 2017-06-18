from django.shortcuts import render
from .models import Song, SongManager
from .forms import UserSongs

def index(request):
    if request.method == 'POST':
        song1 = Song.create(request.POST['songTitle1'])
        song2 = Song.create(request.POST['songTitle2'])
        song3 = Song.create(request.POST['songTitle3'])
        result = SongManager.findBestMatch(song1, song2, song3)
        return render(request, 'result.html', {'result': result})
    else:
        # SongManager.initDB()
        form = UserSongs()
        return render(request, 'index.html', {'form': form})