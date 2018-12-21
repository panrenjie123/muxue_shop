from django.shortcuts import render
from django.views.generic import View
from df_notice.models import Notice
from django.core.paginator import Paginator
# Create your views here.
class HelpView(View):
    def get(self,request):
        return render(request,'df_notice/help.html')

class NoticeView(View):
    def get(self,request,pindex):
        notices = Notice.objects.all().order_by('update_time')
        new_notices = Notice.objects.all().order_by('update_time')[0:6]
        paginator = Paginator(notices,3)
        if pindex == '':
            pindex = 1
        pindex = int(pindex)
        if pindex > paginator.num_pages:
            pindex = paginator.num_pages
        page = paginator.page(pindex)
        page_list = paginator.page_range
        context = {
            'page':page,
            'page_list':page_list,
            'new_notices':new_notices
        }
        return render(request,'df_notice/notice.html',context)

class NoticeDetailView(View):
    def get(self,request,tid):
        notice = Notice.objects.get(id=tid)
        new_notices = Notice.objects.all().order_by('update_time')[0:6]
        notice.browers_number += 1
        notice.save()
        context = {
            'notice':notice,
            'new_notices':new_notices,
        }
        return render(request,'df_notice/notice_detail.html',context)
