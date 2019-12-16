from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render

from .models import Album

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums':all_albums}
    return render(request,'music/index.html',context)
    '''
    template = loader.get_template('music/index.html')
    context = {
        'all_albums':all_albums,
    }
    return HttpResponse(template.render(context, request))
    '''
    '''
    html = ''
    for album in all_albums:
        url= '/music/' + str(album.id )+ '/'
        html += '<a href="'+url+'"> '+album.album_title +'</a><br>'
    return HttpResponse(html)
    '''




def detail(request,album_id):
    return HttpResponse("<h2> Details for Album id : " +str(album_id) +"</h2>")
