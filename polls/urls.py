from django.urls import path
from . import views as polls
from django.conf.urls import url

urlpatterns = [
    # path('first_page/', views.first_page, name='first_page'),
    path('first_page/', polls.first_page, name='first_page'),
    # path('first_page/get_cnty_file/', polls.get_cnty_file),
]