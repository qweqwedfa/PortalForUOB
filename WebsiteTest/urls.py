from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import item_list

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('WebsiteTest.urls')),
    # path("", views.hello, name="hello"),
    path("", item_list, name="item_list"),
    path("portal_test_1/", views.portal_test, name="portal_test"),
    path("demo/", views.demo, name="demo_test"),
    #path('../../reder_demo/', include('reder_demo.urls')),
]