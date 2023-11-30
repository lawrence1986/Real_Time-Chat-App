from django.urls import path
from .views import messages_page, user_login, user_search, start_chat, user_logout, handle_404

urlpatterns = [
    path('messages/', messages_page, name='messages'),
    path('user_login/', user_login, name='login'),
    path('user_search/', user_search, name='user_search'),
    path('user_logout/', user_logout, name='logout'),
    path('user_search/', user_search, name='user_search'),
    path('start_chat/<int:user_id>/', start_chat, name='start_chat'),
    path('404/', handle_404, name='handle_404'),
]
