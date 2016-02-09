from django.shortcuts import render,redirect
from lists.models import ListItem,List
# Create your views here.
def home_page(request):
    # if request.method == 'POST':
    #     ListItem.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'lists/home.html')

def view_list(request):
    items=ListItem.objects.all()
    return render(request,'lists/list.html',{'items':items})


def new_list(request):
    list_ = List.objects.create()
    ListItem.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
