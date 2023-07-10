from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from places.models import Post


def serialize_post(post):
    post = {
        "title": post.title,
        "imgs": [
            f'{pic.image.url}' for pic in post.pics.all().order_by('sequence_number')
        ],
        "description_short": post.short_description,
        "description_long": post.long_description,
        "coordinates": {
            "lng": post.lon,
            "lat": post.lat
        }
    }
    return post


def details_json(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post_data = serialize_post(post)
    return JsonResponse(post_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
