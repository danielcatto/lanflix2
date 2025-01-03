from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from utils.lista_arquivos.main import lista_videos
# Create your views here.
def index(request):    
    vi = lista_videos('media_videos')
    
    print(f'teste vi {vi}')
    print()
    # Fetches all members from the database
    template = loader.get_template('index.html')
    
    context = {
        'vi': vi    }
    return HttpResponse(template.render(context, request))    



def exibir_video(request, nome):
    #clip = VideoFileClip(f'static/videos/{nome}.mp4')
    #clip = VideoFileClip(f'/data/web/media/media_videos')
    #duracao_em_segundos = clip.duration
    
    template = loader.get_template('exibir_video.html')
    context= {
        'nome':nome,
    }
    return HttpResponse(template.render(context))
