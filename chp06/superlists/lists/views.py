from django.shortcuts import render,redirect
from lists.models import ListItem,List
# Create your views here.
def home_page(request):
    # if request.method == 'POST':
    #     ListItem.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'lists/home.html')

def view_list(request,list_id):
    list_=List.objects.get(id=list_id)
    # items=ListItem.objects.filter(list=list_)
    return render(request,'lists/list.html',{'list':list_})


def new_list(request):
    list_ = List.objects.create()
    ListItem.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/'%(list_.id,))

def add_item(request,list_id):
    list_=List.objects.get(id=list_id)
    ListItem.objects.create(text=request.POST['item_text'],list=list_)
    return redirect('/lists/%d/'%(list_.id))
