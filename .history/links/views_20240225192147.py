from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.sessions.models import Session
from links.models import Link

# Create your views here.


def index(request):
    links = Link.objects.all()

    return render(request, "links/index.html", {"links": links})


def root_link(request, link_slug):

    link = get_object_or_404(Link, slug=link_slug)

    return redirect(link.url)
