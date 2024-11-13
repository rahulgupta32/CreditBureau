from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

# from scoring import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scoring.urls')),
    path('', RedirectView.as_view(url='/questions/', permanent=False)),  # Redirect root to questions

    # path('', views.home, name = 'home'),
]
