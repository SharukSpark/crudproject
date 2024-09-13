from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_items')
    else:
        form = ItemForm()
    return render(request, 'create_item.html', {'form': form})

# Read
def list_items(request):
    items = Item.objects.all()
    return render(request, 'list_items.html', {'items': items})

# Update
def update_item(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list_items')
    else:
        form = ItemForm(instance=item)
    return render(request, 'update_item.html', {'form': form})

# Delete
def delete_item(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('list_items')
    return render(request, 'delete_item.html', {'item': item})
