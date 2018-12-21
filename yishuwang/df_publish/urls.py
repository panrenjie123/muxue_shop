from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^publish/$',views.PublishView.as_view()),
    url(r'^once/$',views.OnceView.as_view()),
    url(r'^second_(\d+)/$',views.SecondView.as_view()),
    url(r'^third_(\d+)/$',views.ThirdView.as_view()),
    url(r'^published_(\d+)/$',views.PublishedView.as_view()),
    url(r'^edit_(\d+)/$',views.EditView.as_view()),
    url(r'^delete_(\d+)/$',views.DeleteView.as_view()),
    url(r'^bought_(\d+)/$',views.BoughtView.as_view()),

]