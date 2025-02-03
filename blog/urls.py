from django.urls import path
from .views import main, detail, create_note, delete_nnote,edit_note


urlpatterns = [
    path("", main, name="main"),
    path("<int:note_id>/", detail, name="detail"),
    path("delete/<int:note_id>/", delete_nnote, name="delete"),
    path("create/", create_note, name="create_note"),
    path("edit/<int:note_id>", edit_note, name="edit_note"),
]

