"""Django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from django.conf import settings

from . import views

# 重写内置错误页面
handler500 = 'Django_test.views.page_500'
# 500触发异常、404url不存在、403没有权限、

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^time/$', views.now_time),
    url(r'^article/(?P<year>[0-9]{4})/$', views.article),
    url(r'^now/$', views.now_use_file),

    # 重定向的实验
    url(r'^index1/$', views.index_one, name='i1'),
    url(r'^index2/$', views.index_two, name='i2')
]


# 处理静态资源的url
urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]