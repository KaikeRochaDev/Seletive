from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.empresas),
    path('nova_empresa/', views.nova_empresa, name='nova_empresa'),
    path('empresas/', views.empresas, name='empresa'),
    path('excluir_empresa/<int:id>', views.excluir_empresa, name='excluir_empresa'),
    path('empresa/<int:id>', views.empresa, name='empresa_unica')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
