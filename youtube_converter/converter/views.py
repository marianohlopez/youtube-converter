import os
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
            return JsonResponse({'error': str(e)})
