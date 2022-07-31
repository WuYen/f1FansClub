from django.shortcuts import render
from django.http import HttpResponse
from .models import Team


def index(request):
    data = Team.objects.all().order_by("rank").values()

    if data.count() == 0:
        data = [
            {
                "name": "紅牛車隊",
                "rank": "1",
                "pole": "3",
                "champ": "7",
                "point": "304",
                "icon": "https://pbs.twimg.com/profile_images/1491441516568616972/F0dvwlIp_400x400.jpg",
                "driver": "Verstappen & Pérez",
            },
            {
                "name": "法拉利",
                "rank": "2",
                "pole": "6",
                "champ": "2",
                "point": "228",
                "icon": "https://pbs.twimg.com/profile_images/947659786555940865/P5eYYYIx_400x400.jpg",
                "driver": "Sainz & Leclerc",
            },
        ]

    context = {"teams": data}
    return render(request, "index.html", context)
