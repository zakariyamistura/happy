from django.urls import path
from .views import main, detail, create_note, delete_nnote, edit_note, login_user, create_user, logout_user, land


urlpatterns = [
    path("", land, name="Landing page"),
    path("home/", main, name="main"),
    path("<int:note_id>/", detail, name="detail"),
    path("login/", login_user, name="login_user"),
    path("signup/", create_user, name="create_user"),
    path("delete/<int:note_id>/", delete_nnote, name="delete"),
    path("create/", create_note, name="create_note"),
    path('logout/', logout_user, name="logout"),
    path("edit/<int:note_id>", edit_note, name="edit_note"),
]

