from django.urls import path
from home.views import home
from home.views import detail
from home.views import delete
from home.views import update
from home.views import create

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:todo_id>', detail, name='detail'),
    path('delete/int:<todo_id>', delete, name='delete'),
    path('update/int:<todo_id>', update, name='update'),
    path('create/',create, name='create')
]