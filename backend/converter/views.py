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
            with YoutubeDL(params={'outtmpl': 'media/%(title)s.mp3', 'format': 'bestaudio',
                                   'verbose': True, }) as ydl:
                ydl.download([video_url])

            return HttpResponse(open('media/%(title)s.mp3', 'rb').read(), content_type='audio/mp3')

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON inválido'}, status=400)


@csrf_exempt
def download_video(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            video_url = data.get('video_url')
            output_path = 'media/%(title)s.mp4'

            with YoutubeDL(params={'outtmpl': output_path, 'verbose': True}) as ydl:
                info_dict = ydl.extract_info(video_url, download=True)
                video_filename = ydl.prepare_filename(info_dict)

            with open(video_filename, 'rb') as file:
                response = HttpResponse(file.read(), content_type='video/mp4')
                response['Content-Disposition'] = f'attachment; filename="{info_dict["title"]}.mp4"'
                return response

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON inválido'}, status=400)
