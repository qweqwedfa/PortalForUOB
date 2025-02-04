from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Item

def hello(request):
    text_ = "Hello world !\nThe test website for IBM portal 1."
    return HttpResponse(text_)

def portal_test(request):
    return render(request, "PortalTest.html")

def demo(request):
    return render(request, "render_demo.html")



def item_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        if name and description:
            Item.objects.create(name=name, description=description)
        return redirect("item_list")  # 避免重复提交表单

    items = Item.objects.all()  # 查询数据库中的所有对象
    return render(request, "../templates/render_demo.html", {"items": items})