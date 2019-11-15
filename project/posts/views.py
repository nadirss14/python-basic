from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import datetime

list_post = [
    {'name': 'How to React',
        'user': 'Nadir A. Soza',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076'
     },
    {'name': 'How to React',
        'user': 'Norlang Soza',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1035'
     },
    {'name': 'How to React',
        'user': 'Absalon Blanco',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=500'
     }
]


def list_posts(request):
    response = []
    for post in list_post:
        response.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - {timestamp}</small></p>
            <figure><img src="{picture}"/></figure>
            """.format(**post))
    return HttpResponse('<br>'.join(response))


def list_posts2(request):
    return render(request, 'feed.html', {'posts': list_post})
