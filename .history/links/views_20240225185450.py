from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.sessions.models import Session
from links.models import Link

# Create your views here.


def index(request):
    links = Link.objects.all()

    return render(request, "links/index.html", {"links": links})


def root_link(request, link_slug):

    link = get_object_or_404(Link, slug=link_slug)
    # add the number of times the link  is being clicked

    if "clicked_link" not in request.session["clicked_link"]:
        request.session["clicked_link"] = set()

    if link.id not in request.session["clicked_link"]:
        link.click()
        request.session["clicked_link"].add(id)
    return redirect(link.url)
