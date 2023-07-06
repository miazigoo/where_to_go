from django.shortcuts import render


from django.urls import reverse

from places.models import Post


def serialize_post(post):
    redirect_url = reverse("details-json", args=[post.pk])

    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [post.point_lon, post.point_lat]
        },
        "properties": {
            "title": post.title.split("«")[1],
            "placeId": post.slug,
            "detailsUrl": redirect_url
        }
    }


def index(request):
    posts = Post.objects.all()
    context = {
        'places_posts': {"type": "FeatureCollection",
                         "features": [
                             serialize_post(post) for post in posts
                         ]}
    }
    return render(request, 'index.html', context)

