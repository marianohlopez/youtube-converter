""" import os
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ConvertedVideo


@csrf_exempt
def convert_video(request):
    if request.method == 'POST':
        youtube_url = request.POST.get('youtube_url')
        conversion_type = request.POST.get('conversion_type')

        if not youtube_url or not conversion_type:
            return JsonResponse({'error': 'Invalid input'})

        try:
            video_id = youtube_url.split('v=')[-1]
            file_name = f'{video_id}.{conversion_type}'
            file_path = f'media/converted_files/{file_name}'
            subprocess.run(['youtube-dl', '-x', '--audio-format',
                           conversion_type, '-o', file_path, youtube_url])

            converted_video = ConvertedVideo.objects.create(
                title=video_id, youtube_url=youtube_url, conversion_type=conversion_type, file_path=file_path)
            return JsonResponse({'success': True, 'file_path': file_path})
        except Exception as e:
            return JsonResponse({'error': str(e)}) """

import os
import youtube_dl
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def convert_to_mp3(request):
    if request.method == 'POST':
        # Obtén la URL del video desde el POST data
        video_url = request.POST.get('video_url')

        ydl_opts = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            """             'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }], """

            'outtmpl': 'media/converted_files/%(title)s.%(ext)s',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)

            audio_file_path = ydl.prepare_filename(info_dict)

            return JsonResponse({'message': 'Conversión exitosa', 'audio_file_path': audio_file_path})

    return JsonResponse({'message': 'Método no permitido'}, status=405)
