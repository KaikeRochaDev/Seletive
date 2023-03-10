from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('nova_vaga/', views.nova_vaga, name='nova_vaga'),
    path('vaga/<int:id>', views.vaga, name='vaga'),
    path('nova_tarefa/<int:id_vaga>', views.nova_tarefa, name='nova_tarefa'),
    path('realizar_tarefa/<int:id>', views.realizar_tarefa, name='realizar_tarefa'),
    path('envia_email/<int:id_vaga>', views.envia_email, name="envia_email"),
    path('tecnologia_status/<int:id_vaga>', views.tecnologia_status, name='tecnologia_status'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
