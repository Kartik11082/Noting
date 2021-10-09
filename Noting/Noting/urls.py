from django.contrib import admin
from django.urls import path
from auApp.views import ulogin, ulogout, usignup, uresetPass, deleteNote
from notingApp.views import home, createNote, feedback


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usignup/', usignup, name="usignup"),
    path('ulogin/', ulogin, name="ulogin"),
    path('uresetpass/', uresetPass, name="uresetPass"),
    path("ulogout/", ulogout, name="ulogout"),
    path('', home, name="home"),
    path('createNote/', createNote, name="createNote"),
    path("deleteNote/<int:noteID>", deleteNote, name="deleteNote"),
    path('feedback/', feedback, name="feedback"),
]
