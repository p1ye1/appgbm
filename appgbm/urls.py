from django.urls import path, include
from .views import inicio, base, galeria, register, sidebar_l, sidebar_r, basic, icons, buscar, login, logout, Registro, CustomLoginView
from django.conf import settings
from django.conf.urls.static import static
from .forms import loginForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', inicio, name='inicio'),
    path('galeria/', galeria, name='galeria'),
    path('sidebar_l/', sidebar_l, name='sidebar_l'),
    path('sidebar_r', sidebar_r, name='sidebar_r'),
    path('basic/', base, name='basic'),
    path('icons/', icons, name='icons'),
    path('full/', base, name='full'),
    path('buscar/', buscar, name='buscar'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='app/login.html',authentication_form=loginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/logout.html'), name='logout'),
    path('registro/', Registro.as_view(), name='registro'),
    path('register/', register, name='register'),
]

urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)