from django.http import HttpResponse
from youtube_dl import YoutubeDL
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def download_audio(request):
    video_url = request.POST['video_url']
    with YoutubeDL(params={'outtmpl': 'output/%(title)s.mp3', 'format': 'bestaudio'}) as ydl:
        ydl.download([video_url])

    return HttpResponse(open('output/%(title)s.mp3', 'rb').read(), content_type='audio/mp3')
