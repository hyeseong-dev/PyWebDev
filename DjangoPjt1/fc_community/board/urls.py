from django.urls import path
from . import views


# from django.http import HttpResponse

# def test(request):
#     return HttpResponse('now test')


urlpatterns = [
    path('list/', views.board_list), 
]


