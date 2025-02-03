from django.urls import path
 
from . import views
 
urlpatterns = [
    path("", views.hello, name="hello"),
    path("portal_test_1/", views.portal_test, name="portal_test"),
    path("demo/", views.demo, name="demo_test"),
] 