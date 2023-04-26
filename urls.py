from django.urls import path
from django.urls import include
from easy_level import views

urlpatterns = [
        path('', include('easy_level.urls')),
        path('admin/', admin.site.urls),
]
