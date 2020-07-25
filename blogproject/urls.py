from django.contrib import admin
from django.urls import path, include
import blogapp.views
import django.contrib.auth.urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('accounts/', include('allauth.urls')),
    path('bookkyung/', blogapp.views.bookkyung, name="bookkyung"),
    path('maum/', blogapp.views.maum, name="maum"),
    path('popolo/', blogapp.views.popolo, name="popolo"),
    path('footprint/create/', blogapp.views.create, name="create"),
    path('footprint/update/<int:pk>', blogapp.views.update, name="update"),
    path('footprint/delete/<int:pk>', blogapp.views.delete, name="delete"),
    path('footprint/', blogapp.views.footprint, name="footprint"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)