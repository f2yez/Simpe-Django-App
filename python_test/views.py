from django.shortcuts import render, redirect
from .forms import CreateClient
from .models import Client
import json

# Function for create User.
def create(request):
    data = {}
    # Check if http method is Post to create new client.
    if request.method == 'POST':
        form = CreateClient(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/client/')
        else:
            # Return old form data to render in input fields.
            data['client'] = form.cleaned_data
            data['errors'] = json.loads(form.errors.as_json())
    # Return Template if Http Request is Get.
    return render(request, 'create.html', data)

def list_users(request):
    data = {}
    filter_data = {}
    search_by = request.GET.get('search_by')
    order_by = request.GET.get('order_by')
    keywords = request.GET.get('keywords')
    # Array of Allowed field in filter process.
    allowed_filter = ['client_name', 'email', 'phone_number', 'address']

    # Build filter conditions.
    if search_by and keywords and search_by in allowed_filter:
        filter_data[search_by + "__icontains"] = keywords
    #Build initial Query.
    clients = Client.objects.filter(**filter_data)
    #Create order query.
    if order_by and order_by in allowed_filter:
        clients = clients.order_by(order_by)
    else:
        clients = clients.order_by('-id')
    #Fetch data with final conditions.
    data['clients'] = clients.all()
    return render(request, 'list.html', data)

def edit(request, client_id):
    data = {}
    # Check if client is exist or not, if not exist the form will be create new.
    try:
        client = Client.objects.get(pk=client_id)
        if request.method == 'POST':
            # send new data with client instance to Form update.
            form = CreateClient(request.POST, instance=client)
            if form.is_valid():
                form.save()
                #Override old data with new data after save.
                client = form.cleaned_data
                client['id'] = client_id
                data['success'] = "Record updated successfully"
            else:
                #Return errors for every fields as json.
                data['errors'] = json.loads(form.errors.as_json())

        data['client'] = client
        data['action'] = 'edit'
        return render(request, 'create.html', data)
    except Client.DoesNotExist:
        return redirect('/client/create')
