from django.urls import path
from .views import cargar_inicio, EventoList, EventoCreate, LoginView, LogoutView, RegistroUsuario #,SignUpView, BienvenidaView

urlpatterns = [
    path('', cargar_inicio, name = 'inicio'),
    path('eventos/', EventoList.as_view(), name = 'lista_eventos'),
    path('evento/nuevo/', EventoCreate.as_view(), name = 'nuevo_evento'),
    path('iniciasesion/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logoutsesion/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    #ojo que estoy trabajando abajo :v
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    path('registro/',  RegistroUsuario.as_view(), name='registro'),
    #path('nuevousuario', BienvenidaView.as_view(), name='bienvenida'),
    #path('nuevousuario2', SignUpView.as_view(), name='sign_up'),
   
]