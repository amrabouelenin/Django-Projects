from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from accounts.views import UserListView

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path('passenger/add/',views.SignUp.as_view(), name='add_passenger'),
    path('passengers/',UserListView.as_view(), name='user-list'),
    #path('', auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    #url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    #url(r"signup/$", views.SignUp.as_view(), name="signup"),
]
