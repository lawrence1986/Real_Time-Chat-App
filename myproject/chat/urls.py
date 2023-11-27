from django.urls import path
from .views import messages_page, user_login, user_search, user_logout

urlpatterns = [
    path('messages/', messages_page, name='messages'),
    path('user_login/', user_login, name='login'),
    path('user_search/', user_search, name='user_search'),
    path('user_logout/', user_logout, name='logout'),
    # Other URL patterns
]
