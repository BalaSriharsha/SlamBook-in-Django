from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from . import views
from .forms import LoginForm

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('login/',LoginView.as_view(template_name='slam/login.html',authentication_form=LoginForm,success_url=''),name='login'),
    path('logout/',LogoutView.as_view(template_name='slam/logout.html'),name='logout'),
    path('signup/',views.signup,name='signup'),
    path('<str:user_name>/write_slam/',views.slambook,name='write_slam'),
    path('slambook_submit_success/',views.slambook_submit_success,name='slam_success'),
    path('<int:slam_id>/view_slam/',views.view_slam,name='view_slam'),
    path('generate_pdf/',views.generate_pdf,name='generate_pdf'),
    path('profile/',views.profile,name='profile')
]