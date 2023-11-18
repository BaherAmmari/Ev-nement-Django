from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('i/',views.index),
    path('index/<str:param>',views.index_param),
    path('Affiche/',Affiche,name='Aff'),
    path('Liste/',AfficheGeneric.as_view()),
    path('Detail/<str:title>',Detail,name="D"),
    path('DG/<int:pk>',DetailGeneric.as_view(),name="DD"),
    path('Ajout/',Add,name="Add"),
    path('Add/',Ajout.as_view(),name='Ajout'),
    path('Delete/<int:pk>',Delete.as_view(),name="delete"),
    path('Deletee/<int:id>',Deletee,name="deletee"),
    path('Update/<int:pk>',UpdateGeneric.as_view(),name='Update'),
    
    path('Part/<int:event_id>',Participate,name="Participate"),
    path('Cancel/<int:id>',Cancel,name="Cancel"),
    path('api/',get_Events)

]
