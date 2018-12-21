from django.shortcuts import redirect
from django.http import JsonResponse

#验证用户是否登录
def login_proving(func):
    def login_fun(request,*args,**kwargs):
        #逻辑 判断当前用户是否登录
        if request.session.has_key("_auth_user_id"):
            #将结果返回
            return func(request,*args,**kwargs)
        else:
            #异步请求
            if request.is_ajax():
                return JsonResponse({'islogin':0})
            else:
                return redirect('/user/login/')
    return login_fun