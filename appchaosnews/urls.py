from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomAuthenticationForm
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('noticia/<int:noticia_id>/', views.detalle_noticia, name='detalle_noticia'),
    path('noticia/<int:noticia_id>/editar/', views.editar_noticia, name='editar_noticia'),
    path('noticia/<int:noticia_id>/eliminar/', views.eliminar_noticia, name='eliminar_noticia'),
    path('subir_noticia/', views.subir_noticia, name='subir_noticia'),
    path('buscar/', views.buscar_noticias, name='buscar_noticias'),
    path('noticia/<int:noticia_id>/like/', views.like_noticia, name='like_noticia'),
    path('noticia/<int:noticia_id>/comentar/', views.comentar_noticia, name='comentar_noticia'),
    path('comentario/<int:comentario_id>/like/', views.like_comentario, name='like_comentario'),
    path('perfil/', views.subir_perfil, name='perfil'),
    path('perfil/<int:user_id>/', views.subir_perfil, name='perfil_with_id'),  # Agrega esta línea
]

# notas
