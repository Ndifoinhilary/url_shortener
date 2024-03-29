from django.urls import path

from links.views import index, root_link


urlpatterns = [
    path("", index, name="home"),
    path("<str:link_slug>/", root_link, name="link"),
]
