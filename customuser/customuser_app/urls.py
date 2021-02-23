from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'customuser_app'

urlpatterns = [
    path('passenger/add/',views.SignUp.as_view(), name='add_passenger'),
    #path('', auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    #url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    #url(r"signup/$", views.SignUp.as_view(), name="signup"),
]
