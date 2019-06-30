from django.urls import path
from django.urls import re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="login.html"), name='task1-login'),
    path('logout', auth_views.LogoutView.as_view(next_page="/"), name='task1-logout'),
    path('main', views.main),
    path('some', views.answer, name='answer'),
    # re_path(r'^signup/$', views.signup, name='signup'),
    # path('click', views.click, name='task1-click'),
    re_path(r'^(?P<test_id>\d+)/click/', views.click, name='task1-click')
]