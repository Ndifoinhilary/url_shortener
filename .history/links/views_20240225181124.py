from django.shortcuts import get_object_or_404, render

from links.models import Link

# Create your views here.


def index(request):
    links = Link.objects.all()

    context = {"links": links}

    return render(request, "links/index.html", context)


def root_link(request, link_slug):

    link = get_object_or_404(Link, slug=link_slug)
    # add the number of times the link  is being clicked

    link.clicks()
