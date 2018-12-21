from django.shortcuts import render,redirect
from django.views.generic import View
from df_goods.models import BookInfo,TypesInfo,Grade
from df_user.models import University,Career,College
from django.core.paginator import Paginator
from df_notice.models import Notice
from django.http import JsonResponse
from django.db import transaction
from datetime import datetime
from df_publish.models import Order
from df_user.decorator import login_proving
from django.utils.decorators import method_decorator
# Create your views here.

class IndexView(View):
    def get(self,request):
        #教材书展示
        #教材书类二级分类
        second = TypesInfo.objects.filter(parent_id = 1)
        data = []
        for item in second:
            third = TypesInfo.objects.filter(parent_id = item.id)
            data.append({
                'second':item,
                'third_list':third,
            })
        # 教材书展示
        education_books = BookInfo.objects.all().order_by('id')[0:12]
        #工具书展示
        #英语四六级资料
        reference_books_yingyu = BookInfo.objects.filter(types_id = 45).order_by('id')[0:7]
        #公务员资料
        reference_books_gongwu = BookInfo.objects.filter(types_id=46).order_by('id')[0:7]
        #考研资料
        reference_books_kaiyan = BookInfo.objects.filter(types_id=47).order_by('id')[0:7]
        #雅思托福
        reference_books_yasi = BookInfo.objects.filter(types_id=48).order_by('id')[0:7]
        #其他
        reference_books_qita = BookInfo.objects.filter(types_id=49).order_by('id')[0:7]
        #推荐
        recommended_books = BookInfo.objects.filter(share_book__isnull = False).order_by('-id')[0:14]
        #最新公告
        new_notices = Notice.objects.all().order_by('update_time')[0:5]
        context = {
            'data':data,
            'education_books':education_books,
            'reference_books_yingyu':reference_books_yingyu,
            'reference_books_gongwu':reference_books_gongwu,
            'reference_books_kaiyan':reference_books_kaiyan,
            'reference_books_yasi':reference_books_yasi,
            'reference_books_qita':reference_books_qita ,
            'recommended_books':recommended_books,
            'new_notices':new_notices
        }
        return render(request,'df_goods/index.html',context)

class DetailView(View):
    def get(self,request,tid):
        #获取当前图书id
        book_detail = BookInfo.objects.get(id=tid)
        #同类推荐
        same_books = BookInfo.objects.filter(types_id=book_detail.types_id)[0:5]
        context = {
            'book_detail':book_detail,
            'same_books':same_books,
        }
        return render(request,'df_goods/detail.html',context)

@method_decorator(login_proving,name='get')
class AddView(View):
    def get(self,request,bid):
        book = BookInfo.objects.get(id=bid)
        # 设置保存点
        sid = transaction.savepoint()
        try:
            order_1 = Order()
            user_id = request.session['_auth_user_id']
            order_1.user_id = user_id
            now_time = datetime.now()
            order_1.create_time = now_time
            time_user = '%s%d' % (now_time.strftime('%Y%m%d%H%M%S'), int(user_id))
            order_1.order_id = time_user
            order_1.total = book.price
            order_1.books_id = bid
            if book.number >= 1:
                book.number -= 1
                book.save()
            else:
                transaction.savepoint_rollback(sid)
                return JsonResponse({'msg':'库存不足'})
            order_1.save()
            return JsonResponse({'msg': '添加成功', 'counts': book.number})
        except:
            transaction.savepoint_rollback(sid)
            return JsonResponse({'msg':'添加失败'})

class ListView(View):
    def get(self,request,tid,pindex):
        #过滤条件
        university = University.objects.all()
        career = Career.objects.all()
        college = College.objects.all()
        grade = Grade.objects.all()
        #当点击我要买时，应显示所有图书信息，默认传过来的值为0，
        if tid == '0':
            books = BookInfo.objects.all().order_by('id')
        #通过前端点击分类，获取分类id，从而获取值
        else:
            books = BookInfo.objects.filter(types_id = tid ).order_by('id')
        #分页，每页14本书
        paginator = Paginator(books,14)
        if pindex == '':
            pindex = 1
        pindex = int(pindex)
        #当页码大于最大页时，页码为最大页
        if pindex>paginator.num_pages:
            pindex = paginator.num_pages
        #每页的书籍信息
        page = paginator.page(pindex)
        #分多少页
        page_list = paginator.page_range
        context = {
            'page':page,
            'page_list':page_list,
            'university':university,
            'college':college,
            'career':career,
            'grade':grade,
            'tid':tid,
        }
        return render(request,'df_goods/list.html',context)





