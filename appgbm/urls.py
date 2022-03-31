from django.urls import path, include
from .views import index, base, galeria, sidebar_l, sidebar_r, basic, icons, buscar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='inicio'),
    path('galeria/', galeria, name='galeria'),
    path('sidebar_l/', sidebar_l, name='sidebar_l'),
    path('sidebar_r', sidebar_r, name='sidebar_r'),
    path('basic/', base, name='basic'),
    path('icons/', base, name='icons'),
    path('full/', base, name='full'),
    path('buscar/', buscar, name='buscar')
]

urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)