from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.IndexView.as_view()),
    url(r'^detail_(\d+)/$',views.DetailView.as_view()),
    url(r'^list_(\d+)_(\d+)/$',views.ListView.as_view()),
    url(r'^add_(\d+)/$',views.AddView.as_view()),
]