from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.

# def index(request):
#     items = Item.objects.all()
#     return render( request, 'Main/index.html', { 'items': items })


class IndexClassView(ListView):
    model = Item;
    template_name = 'Main/index.html'
    context_object_name = 'items'

# def detail(request, item_id):
#     item = Item.objects.get(pk = item_id)
#     return render( request, 'Main/detail.html', { 'item': item } )

class DetailClassView(DetailView):
    model = Item;
    template_name = 'Main/detail.html'



# def AddItems(request):
#     form = ItemForm( request.POST or None )
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')

#     return render(request, 'Main/add_items.html', { 'form':form })

class CreateItems(CreateView):
    model = Item;
    fields = ['item_name', 'item_description', 'item_price', 'item_image']
    template_name = 'Main/add_items.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)

def UpdateItems(request, item_id):
    item = Item.objects.get(pk = item_id)
    form = ItemForm(request.POST or None, instance = item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render( request, 'Main/update_items.html', { 'form':form , 'item': item } )
    
def DeleteItems(request, item_id):
    item = Item.objects.get(pk = item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'Main/delete_items.html', {'item': item})