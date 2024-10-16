from django.urls import path
from accounts.views import user_rgeister
from accounts.views import user_login
from accounts.views import user_logout
# from accounts.views import update
# from accounts.views import create

urlpatterns = [
    path('rgeister/', user_rgeister, name='user_rgeister'),
    path('login/', user_login, name = 'login'),
    path('logout/', user_logout, name = 'logout'),
]