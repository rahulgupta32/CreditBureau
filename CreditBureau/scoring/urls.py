from django.urls import path
from .views import question_view, home_view

urlpatterns = [
    # path('login/',views.custom_login, name = 'login'),
    # path('logout/',views.custom_logout, name = 'logout'),
    # path('form/', views.form_page, name='form_page'),
    # path('results/', views.results_page, name='results_page'),
    # path('', views.home, name='home'),  # New pattern for the root URL
    path('questions/', question_view, name='questions'),
    # path('questions/', question_view, name='questions'),  # Questions page

    path('', home_view, name='home'),  # Add this line for the home page

]
