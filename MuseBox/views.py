from django.shortcuts import render
from .models import SongManager
from .forms import UserSongs

def index(request):
    if request.method == 'POST':
        result = SongManager.findBestMatch(request.POST.get('songTitle1'), request.POST.get('songTitle2'), request.POST.get('songTitle3'))
        return render(request, 'result.html', {'result': result})
    else:
        #SongManager.initDB()
        form = UserSongs()
        return render(request, 'index.html', {'form': form})