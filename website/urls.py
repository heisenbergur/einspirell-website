from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import people.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',people.views.index, name='index'),
    path('team/',people.views.team, name='team'),
    path('Demo/',people.views.Demo, name='Demo'),
    path('courses/', include('courses.urls')),
    path('contact/',people.views.contact, name='contact'),
    path('culture/',people.views.culture, name='culture'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
