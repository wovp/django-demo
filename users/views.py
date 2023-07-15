from hashlib import md5

from django.db.models.query import EmptyQuerySet
from django.shortcuts import render
from django.views import View

from users.models import VerifyLogin, UserProfile


# Create your views here.
class LoginView(View):
    def post(self, request):
        lo_data = request.POST
        lo_username = lo_data.get('username')
        lo_password = lo_data.get('password')
        lo_object = UserProfile.objects.filter(username=lo_username, password=lo_password)
        response = render(request, 'index.html')
        if lo_object.exists():
            # 密码正确
            # TODO: 这里的md5加密没搞起来，就简化了一下，直接拼接了
            # ve_encode = md5((lo_username + lo_password).encode(encoding='utf-8').hexdigest())
            ve_encode = lo_username + lo_password
            print("登录成功")
            # 准备储存cookie登录凭证
            if VerifyLogin.objects.filter(username=lo_username, verifying=ve_encode).exists() is False:
                ve_object = VerifyLogin(username=lo_username, verifying=ve_encode)
                response.set_cookie('username', lo_username)
                response.set_cookie('verify_code', ve_encode)
                ve_object.save()
            else:
                response.set_cookie(lo_username, ve_encode)
                # 刷新登陆时间
        else:
            response.write("msg:error")
        return response


class LogoutView(View):
    def get(self, request):
        request.COOKIES.clear()
        response = render(request, 'login.html')
        response.set_cookie('username', '')
        response.set_cookie('verify_code', '')
        return response


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        re_user = UserProfile(username=request.POST.get('username'), password=request.POST.get('password'))
        re_user.save()
        return render(request, 'login.html')


class VerifyLoginView(View):
    def get(self, request):
        ve_cookie = request.COOKIES
        if ve_cookie is None:
            return render(request, 'login.html')
        ve_username = ve_cookie.get('username')
        ve_code = ve_cookie.get('verify_code')
        if ve_username is None or ve_code is None:
            return render(request, 'login.html')
        print("ve_username")
        print(ve_username)
        print(ve_code)

        ve_object = VerifyLogin.objects.filter(username=ve_username, verifying=ve_code)
        print(ve_object.exists())
        if ve_object.exists():
            return render(request, 'index.html')
        return render(request, 'login.html')
