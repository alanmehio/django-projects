from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.views import generic, View
from .forms import TodoForm
from .models import Todo

'''
# Create your views here.
def index(request):
    print ("enbter index ...")
    item_list = Todo.objects.order_by("-date")
    if request.method == 'POST':
        print("methiod is post inside index")
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            print(redirect('/todo')) # it gives this  <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/todo">
            return redirect(reverse('todo:index')) # this cause a get to the same page /todo  skip the post and goes to render the template. revers casuse a problem 
          
    form = TodoForm()
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    print("return the templated rendering it ..")
    return render(request, 'todo/index.html', page) # template to render

def remove(request, item_id):
    print("enter remove now ...")
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!!")
    print(reverse('todo:index')) # it shows '/todo' it obtain the path by giving the name in the urlpatterns
    return   redirect(reverse('todo:index')) # reverse gives you the path defined un the urlpatterns  given the name so revers('todo:index') gives /todo
'''

class IndexView(View):
    form_class = TodoForm
    template_name = 'todo/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        item_list = Todo.objects.order_by("-date")
        page = {
            "forms": form,
            "list": item_list,
            "title": "TODO LIST",
        }

        return render(request,self.template_name,page)
    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if(form.is_valid()):
           form.save()
           return redirect(reverse('todo:index'))
       
        item_list = Todo.objects.order_by("-date")
        page = {
            "forms": form,
            "list": item_list,
            "title": "TODO LIST",
            }
       
        return render(request, self.template_name, page)
    

def remove(request, item_id):
    print("enter remove now ...")
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!!")
    print(reverse('todo:index')) # it shows '/todo' it obtain the path by giving the namne in the urlpatterns
    return   redirect(reverse('todo:index')) # reverse gives you the path defined un the urlpatterns  given the name so revers('todo:index') gives /todo