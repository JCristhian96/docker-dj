from django.urls import path
# Views Core
from . import views

app_name = "core"

urlpatterns = [
    path(
        '',
        views.Index.as_view(),
        name="index"
    ),
    path(
        'person/list/',
        views.PersonListView.as_view(),
        name="list"
    ),
    path(
        'person/add/',
        views.PersonCreateView.as_view(),
        name="add"
    ),
    path(
        'person/update/<pk>/',
        views.PersonUpdateView.as_view(),
        name="update"
    ),
    path(
        'person/delete/<pk>/',
        views.PersonDeleteView.as_view(),
        name="delete"
    ),
]
