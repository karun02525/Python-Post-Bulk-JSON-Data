from django.urls import path
from .views import home,get,create,create_bulk
urlpatterns = [
    path('',home),
    path('get-student',get),
    path('student',create),
    path('create-bulk-student',create_bulk)
]
