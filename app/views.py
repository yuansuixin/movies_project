import hashlib

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app.models import User, Banner, Movies, Like


#主页
def home(request):
    username = request.session.get('username')
    data={
        'title':'微电影',
    }

    # 登录注册的显示
    if username:
        user = User.objects.get(u_name=username)
        data['username'] = username
        data['islogin'] = 'login'
        data['icon'] = user.u_icon.url

    #     加载banner图
    banners = Banner.objects.all()
    data['banners'] = banners

    # 加载电影
    movies = Movies.objects.all()
    data['movies'] = movies

    return render(request,'app/home/home.html',context=data)

# 注册页面
def register(request):
    # 使用的是聚合，通过表单的method来判断
    if request.method=='POST':
        # 获取到提交的数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('password',password)
        repassword = request.POST.get('repassword')
        icon = request.FILES['icon']

        user = User()
        user.u_name = username
        password = password2md5(password)
        print('摘要后',password)
        user.u_password= password
        user.u_icon = icon
        user.save()
        print('用户注册成功')
    #     设置session缓存
        request.session['username']=username
        response = redirect(reverse('app:home'))
        return response
    elif request.method=='GET':
        return render(request,'app/home/register.html')


# md5摘要
def password2md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

# ajax用户检测
def checkuser(request):
    username = request.GET.get('username')
    users = User.objects.filter(u_name=username)
    print('检测用户名')
    data = {
        'msg':'用户名可用',
        'status':'888'
    }
    if users.exists():
        data['msg'] = '用户名已存在'
        data['status'] = '900'
    return JsonResponse(data)

# 登录
def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        print('username',username)
        password = request.POST.get('password')
        users = User.objects.filter(isDelete=False).filter(u_name=username)
        # users = User.objects.filter(isDelete=False).filter(email=username)
        print('长度',len(users))
        if users.exists():
            user = users.first()
            u_password = user.u_password
            password = password2md5(password)
            if u_password == password:
                request.session['username'] = username
                return redirect(reverse('app:home'))

        return render(request,'app/home/login.html',{'testlogin':'用户名或密码错误'})
    elif request.method == 'GET':
        return render(request,'app/home/login.html')


# def login(request):
#     if request.method=='POST':
#         username = request.POST.get('username')
#         print('username',username)
#         password = request.POST.get('password')
#         users = User.objects.filter(isDelete=False).filter(u_name=username)
#         if not users.exists():
#             users_e = User.objects.filter(isDelete=False).filter(email=username)
#             print('u_name',users_e.first().u_name)
#             print('长度',len(users_e))
#             user = users_e.first()
#             u_password = user.u_password
#             password = password2md5(password)
#             print(password,'----password')
#             if u_password == password:
#                 print(password, '----password相等')
#                 request.session['username'] = username
#                 return redirect(reverse('app:home'))
#         if users.exists():
#             user = users.first()
#             u_password = user.u_password
#             password = password2md5(password)
#             if u_password == password:
#                 request.session['username'] = username
#                 return redirect(reverse('app:home'))
#
#         return render(request,'app/home/login.html',{'testlogin':'用户名或密码错误'})
#     elif request.method == 'GET':
#         return render(request,'app/home/login.html')










# 收藏,将电影添加到收藏页面
def addlike(request):
    username = request.session.get('username')
    data={
        'status':'200',
        'msg':'ok',
    }
    if not username:
        data['status'] = '302'
        data['msg'] = '用户未登录'
        print('用户未登录')
        return JsonResponse(data)
    moviesid = request.GET.get('id')
    print(moviesid)
    movie = Movies.objects.filter(pk=moviesid).first()
    print('movie',movie)
    user = User.objects.filter(u_name=username).first()
    love_item = Like.objects.filter(like_user=user).filter(like_movies=movie).first()
    print('love_item',love_item)

    if not love_item:
        love_item = Like()
        love_item.like_user = user
        love_item.like_movies=movie
        love_item.save()
        movie.like_num+=1
        movie.save()
    else:
        love_item.delete()
        movie.like_num-=1
        movie.save()
    data['num'] = movie.like_num
    return JsonResponse(data)




def like(request):
    username = request.session.get('username')
    data = {
        'title': '微电影',
    }

    if not username:
        return redirect(reverse('app:login'))
    user = User.objects.filter(u_name=username).first()
    # 登录注册的显示
    if username:
        data['username'] = username
        data['islogin'] = 'login'
        data['icon'] = user.u_icon.url

    # 加载banner图
    banners = Banner.objects.all()
    data['banners'] = banners

    # 加载电影
    # movies = user.like_set.all()
    movies = Like.objects.filter(like_user=user)
    print(movies)
    print('长度',len(movies))
    data['movies'] = movies
    return render(request,'app/home/like.html',context=data)




def userinfo(request):
    username = request.session.get('username')
    if request.method=='POST':
        users = User.objects.filter(u_name=username)
        if users.exists():
            user = users.first()
            user.email = request.POST.get('email')
            user.u_icon = request.FILES.get('icon')
            print(user.u_icon)
            user.save()
            print(user.email)
            print('postpostpost')
            resp = redirect(reverse('app:home'))
            return resp
    elif request.method=='GET':
        user = User.objects.filter(u_name=username).first()
        print('getgetget')
        data = {
            'username':username,
        }
        return render(request,'app/home/userinfo_mod.html',data)

# 退出登录
def logout(request):
    request.session.flush()
    return redirect(reverse('app:home'))