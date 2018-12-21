from django.conf.urls import url

from . import views

urlpatterns = [
    url('help/',views.HelpView.as_view()),
    url(r'^notice_(\d+)/$',views.NoticeView.as_view()),
    url(r'^notice_detail_(\d+)/$',views.NoticeDetailView.as_view()),
]