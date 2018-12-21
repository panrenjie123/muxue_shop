from django.http import HttpResponse,HttpRequest

class Url:
    def process_response(self,request,response):
        url_list = [
            "/user/login/",
            "/user/register/"
        ]
        if not request.is_ajax() and request.path not in url_list:
            # request.get_full_path() -- 获取当前url,(包含参数) 200/?type=10
            #   request.path --  获取当前url,(但不含参数) /200/
            response.set_cookie("redirect_url",request.get_full_path())
        return  response