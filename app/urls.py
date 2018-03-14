from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^home/$',views.home,name='home'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
#     用于异步请求的时候用户名的检测
    url(r'^checkuser/$',views.checkuser,name='checkuser'),
# 收藏
    url(r'^addlike/$',views.addlike,name='addlike'),
    url(r'^like/$', views.like, name='like'),
    #  用户信息修改
    url(r'^userinfo/$',views.userinfo,name='userinfo'),

]
