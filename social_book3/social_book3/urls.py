from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core_app1 import views

urlpatterns = [
    path("admin123/", admin.site.urls),
    path("", include("core_app1.urls")), 
    path('setting/', views.settings_view, name='setting'), 
    path('create_post/', views.create_post, name='create_post'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)