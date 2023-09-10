from django.http import HttpResponse, JsonResponse
from youtube_dl import YoutubeDL
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def download_audio(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            video_url = data.get('video_url')
            print(video_url)
            with YoutubeDL(params={'outtmpl': 'output/%(title)s.mp3', 'format': 'bestaudio'}) as ydl:
                ydl.download([video_url])

            return HttpResponse(open('output/%(title)s.mp3', 'rb').read(), content_type='audio/mp3')

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON inválido'}, status=400)
