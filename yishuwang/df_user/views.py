from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import authenticate,logout,login
from .models import University,College,Career,UserInfo
from django.contrib.auth.hashers import make_password,check_password
from django.http import JsonResponse
from df_user.decorator import login_proving
from django.utils.decorators import method_decorator
# Create your views here.

class LoginView(View):
    def get(self,request):
        #获取登陆后的用户名
        username = request.COOKIES.get('username','')
        context = {
            'username':username
        }
        return render(request,'df_user/login.html',context)
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_login = authenticate(username=username,password=password)
        if user_login is not None:
            #写session用户认证成功，登录成功
            login(request,user_login)
            #重定向
            # url = request.COOKIES.get('redirect_url','/')
            # res = redirect(url)
            # res.set_cookie('redirect_url','',max_age=-1)
            #获取记住用户名 默认为0
            res = redirect('/')
            remember = request.POST.get('remember',0)
            if remember != 0:
                #记住用户名
                res.set_cookie('username',username)
            return res
        else:
            user_info = '用户或密码错误'
            return render(request,'df_user/login.html',{'user_info':user_info})


class RegisterView(View):
    def get(self,request):
        # 注册页使用的内容
        university = University.objects.all()
        college = College.objects.all()
        career = Career.objects.all()
        context = {
            'university': university,
            'college': college,
            'career': career,
        }
        return render(request,'df_user/register.html',context)
    def post(self,request):
        usernamesignup = request.POST.get('usernamesignup')
        phonesignup = request.POST.get('phonesignup')
        university_signup = request.POST.get('university_signup')
        university_id = University.objects.filter(title=university_signup)[0].id
        college_signup = request.POST.get('college_signup')
        college_id = College.objects.filter(title=college_signup)[0].id
        career_signup = request.POST.get('career_signup')
        career_id = Career.objects.filter(title=career_signup)[0].id
        passwordsignup = request.POST.get('passwordsignup')
        #实例化一个对象
        new_user = UserInfo()
        new_user.username = usernamesignup
        new_user.password = make_password(passwordsignup)
        new_user.phone = phonesignup
        new_user.university_id = university_id
        new_user.college_id = college_id
        new_user.career_id = career_id
        new_user.save()
        return redirect('/user/login/')

#验证用户是否存在
class Register_Confirm(View):
    def get(self,request):
        username = request.GET.get('username')
        user = UserInfo.objects.filter(username=username)
        if len(user) == 1:
            return JsonResponse({'result':'ok'})
        else:
            return JsonResponse({'result': 'false'})

#退出登录
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/user/login/')

@method_decorator(login_proving,name='get')
@method_decorator(login_proving,name='post')
class PasswordView(View):
    def get(self,request):
        return render(request,'df_user/password.html')
    def post(self,request):
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        new_password_1 = request.POST.get('new_password_1')
        users = UserInfo.objects.get(id = request.session['_auth_user_id'])
        if users.check_password(old_password):
            if new_password == new_password_1:
                users.password = make_password(new_password)
                users.save()
                return render(request,'df_user/password.html',{'info':'修改成功'})
            else:
                return render(request, 'df_user/password.html', {'info': '两次密码不一致'})
        else:
            return render(request, 'df_user/password.html', {'info': '原密码错误'})


@method_decorator(login_proving,name='get')
@method_decorator(login_proving,name='post')
class CenterView(View):
    def get(self,request):
        userinfo = UserInfo.objects.get(id = request.session['_auth_user_id'])
        university = University.objects.all()
        college = College.objects.all()
        career = Career.objects.all()
        context = {
            'userinfo':userinfo,
            'university':university,
            'college':college,
            'career':career,
        }
        return render(request, 'df_user/member.html',context)
    def post(self,request):
        nickname = request.POST.get('nickname')
        phone = request.POST.get('phone')
        university = request.POST.get('university')
        university_id = University.objects.filter(title=university)[0].id
        college = request.POST.get('college')
        college_id = College.objects.filter(title=college)[0].id
        career = request.POST.get('career')
        career_id = Career.objects.filter(title=career)[0].id
        grade = request.POST.get('grade')
        userinfo = UserInfo.objects.get(id=request.session['_auth_user_id'])
        userinfo.nickname = nickname
        userinfo.phone = phone
        userinfo.university_id = university_id
        userinfo.college_id = college_id
        userinfo.career_id = career_id
        userinfo.grade = grade
        userinfo.save()
        university = University.objects.all()
        college = College.objects.all()
        career = Career.objects.all()
        context = {
            'userinfo': userinfo,
            'university': university,
            'college': college,
            'career': career,
        }
        return render(request, 'df_user/member.html',context)

