from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$',views.LoginView.as_view()),
    url(r'^register/$',views.RegisterView.as_view()),
    url(r'^check/$',views.Register_Confirm.as_view()),
    url(r'^logout/$',views.LogoutView.as_view()),
    url(r'^password/$',views.PasswordView.as_view()),
    url(r'^center/$',views.CenterView.as_view()),
]