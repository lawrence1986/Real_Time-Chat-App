from django.urls import path
from .views import messages_page, user_login, user_logout, handle_404, home

urlpatterns = [
    path('messages/', messages_page, name='messages'),
    path('user_login/', user_login, name='login'),
    path('user_logout/', user_logout, name='logout'),
    path('404.html', handle_404, name='handle_404'),
    path('home/', home, name='home')
]
