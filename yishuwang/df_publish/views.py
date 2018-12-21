from django.shortcuts import render,redirect
from django.views.generic import View
from df_goods.models import TypesInfo,Grade
from df_user.models import UserInfo,University,Career,College
from df_goods.models import BookInfo
from df_publish.models import Order
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime
from django.core.paginator import Paginator
from df_user.decorator import login_proving
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(login_proving,name='get')
@method_decorator(login_proving,name='post')
class PublishView(View):
    def get(self,request):
        university = University.objects.all()
        college = College.objects.all()
        career = Career.objects.all()
        grade = Grade.objects.all()
        context = {
            'university':university,
            'college':college,
            'career':career,
            'grade':grade,
        }
        return render(request,'df_publish/publish.html',context)
    def post(self,request):
        user_id = request.session['_auth_user_id']
        university = request.POST.get('university')
        university_id = University.objects.filter(title=university)[0].id
        college = request.POST.get('college')
        college_id = College.objects.filter(title=college)[0].id
        career = request.POST.get('career')
        career_id = Career.objects.filter(title=career)[0].id
        grade = request.POST.get('grade')
        grade_id = Grade.objects.filter(title=grade)[0].id
        types = request.POST.get('types')
        types_id = TypesInfo.objects.filter(type_name=types)[0].id
        bookname = request.POST.get('bookname')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        number = request.POST.get('number')
        picture = request.FILES.get('picture')
        picture_path = "books/" + picture.name
        file_name = settings.MEDIA_ROOT + "/books/" + picture.name
        with open(file_name,'wb') as pic:
            for c in picture.chunks():
                pic.write(c)
        #实例化一个对象
        book = BookInfo()
        book.bookname = bookname
        book.picture = picture_path
        book.price = price
        book.number = number
        book.university_id = university_id
        book.college_id = college_id
        book.career_id = career_id
        book.grade_id = grade_id
        book.types_id = types_id
        book.share_book_id = user_id
        book.desc = desc
        book.save()
        return redirect('/publish/published_1/')

class OnceView(View):
    def get(self,request):
        one_list = TypesInfo.objects.filter(parent__isnull = True)
        list_one = []
        for item in one_list:
            list_one.append([item.id,item.type_name])
        return JsonResponse({'data':list_one})

class SecondView(View):
    def get(self,request,tid):
        two_list = TypesInfo.objects.filter(parent_id = tid)
        list_two = []
        for item in two_list:
            list_two.append([item.id,item.type_name])
        return JsonResponse({'data':list_two})

class ThirdView(View):
    def get(self,request,tid):
        three_list = TypesInfo.objects.filter(parent_id = tid)
        list_three = []
        for item in three_list:
            list_three.append([item.id,item.type_name])
        return JsonResponse({'data':list_three})

@method_decorator(login_proving,name='get')
class PublishedView(View):
    def get(self,request,pindex):
        books = BookInfo.objects.filter(share_book_id = request.session['_auth_user_id']).order_by('-id')
        paginator = Paginator(books,5)
        if pindex == '':
            pindex = 1
        pindex = int(pindex)
        if pindex>paginator.num_pages:
            pindex = paginator.num_pages
        page = paginator.page(pindex)
        page_list = paginator.page_range
        context = {
            'page':page,
            'page_list':page_list,
        }
        return render(request,'df_publish/published.html',context)

@method_decorator(login_proving,name='get')
@method_decorator(login_proving,name='post')
class EditView(View):
    def get(self,request,tid):
        book = BookInfo.objects.get(id=tid)
        types_three_name = TypesInfo.objects.filter(id=book.types_id)[0].type_name
        types_two_id = TypesInfo.objects.filter(id=book.types_id)[0].parent_id
        types_two_name = TypesInfo.objects.filter(id=types_two_id)[0].type_name
        types_one_id = TypesInfo.objects.filter(id=types_two_id)[0].parent_id
        types_one_name = TypesInfo.objects.filter(id=types_one_id)[0].type_name
        print(types_three_name,types_two_name,types_one_name)
        university = University.objects.all()
        college = College.objects.all()
        career = Career.objects.all()
        grade = Grade.objects.all()
        context = {
            'book':book,
            'university': university,
            'college': college,
            'career': career,
            'grade': grade,
            'types_one_name':types_one_name,
            'types_two_name': types_two_name,
            'types_three_name': types_three_name,
        }
        return render(request,'df_publish/edit.html',context)
    def post(self,request,tid):
        book = BookInfo.objects.get(id=tid)
        university = request.POST.get('university')
        university_id = University.objects.filter(title=university)[0].id
        college = request.POST.get('college')
        college_id = College.objects.filter(title=college)[0].id
        career = request.POST.get('career')
        career_id = Career.objects.filter(title=career)[0].id
        grade = request.POST.get('grade')
        grade_id = Grade.objects.filter(title=grade)[0].id
        types = request.POST.get('types')
        types_id = TypesInfo.objects.filter(type_name=types)[0].id
        bookname = request.POST.get('bookname')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        number = request.POST.get('number')
        picture = request.FILES.get('picture')
        if picture:
            picture_path = "books/" + picture.name
            book.bookname = bookname
            book.picture = picture_path
            book.price = price
            book.number = number
            book.university_id = university_id
            book.college_id = college_id
            book.career_id = career_id
            book.grade_id = grade_id
            book.types_id = types_id
            book.desc = desc
            book.save()
            file_name = settings.MEDIA_ROOT + "/books/" + picture.name
            with open(file_name, 'wb') as pic:
                for c in picture.chunks():
                    pic.write(c)
        else:
            book.bookname = bookname
            book.price = price
            book.number = number
            book.university_id = university_id
            book.college_id = college_id
            book.career_id = career_id
            book.grade_id = grade_id
            book.types_id = types_id
            book.desc = desc
            book.save()
        return redirect('/publish/published_1/')

@method_decorator(login_proving,name='get')
class DeleteView(View):
    def get(self,request,tid):
        BookInfo.objects.get(id=tid).delete()
        return redirect('/publish/published_1/')

@method_decorator(login_proving,name='get')
class BoughtView(View):
    def get(self,request,pindex):
        user_id = request.session['_auth_user_id']
        orders = Order.objects.filter(user_id=user_id).order_by('-create_time')
        order_list = []
        for item in orders:
            if item.isPay == True:
                item.pay_status = 'success'
            else:
                now_time = datetime.now()
                seconds = (now_time - item.create_time).seconds
                if seconds>1800:
                    item.pay_status = 'close'
                else:
                    item.pay_status = 'paying'
            item.save()
            order_list.append(item)
        paginator = Paginator(order_list, 5)
        if pindex == '':
            pindex = 1
        pindex = int(pindex)
        if pindex > paginator.num_pages:
            pindex = paginator.num_pages
        page = paginator.page(pindex)
        page_list = paginator.page_range
        context = {
            'page': page,
            'page_list': page_list,
        }
        return render(request,'df_publish/bought.html',context)