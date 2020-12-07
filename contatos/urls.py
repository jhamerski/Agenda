from django.urls import path
from . import views


urlpatterns = [
    # chama a função index dentro da views
    path('', views.index, name='index'),
    # chama a função ver_contato dentro da views
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
    # chama a url busca/ com a funcao busca da views
    path('busca/', views.busca, name='busca'),
]
