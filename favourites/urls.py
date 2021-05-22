from django.urls import path
from . import views

urlpatterns = [
    path('favourites/', views.view_fav, name='favourites'),
    path('addremove/<item_id>/', views.add_remove_favourites,
         name='add_remove_favourites'),
]
