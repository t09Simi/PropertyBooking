from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from property.models import Property, Room
from property.forms import RegisterForm
# Create your views here.
# Home page
def home(request):
    room_type = Room.objects.values('room_type').distinct()
    location = Property.objects.values('neighbourhood_group').distinct()

    search_query = request.GET.get('search', '')
    location_query = request.GET.getlist('location')
    room_type_query = request.GET.get('room_type', '')
    sort_by = request.GET.get('sort_by', '')

    rooms = Room.objects.all()

    if search_query:
        rooms = rooms.filter(property__name__icontains=search_query)

    if location_query:
        rooms = rooms.filter(property__neighbourhood_group__in=location_query)

    if room_type_query:
        rooms = rooms.filter(room_type=room_type_query)

    if sort_by:
        if sort_by == 'ASC':
            rooms = rooms.order_by('price')
        elif sort_by == 'DSC':
            rooms = rooms.order_by('-price')

    paginator = Paginator(rooms, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'room_type': room_type,
        'location': location,
        'page_obj': page_obj,
        'search': search_query,
        'sort_by': sort_by,
    }

    return render(request, 'property/home.html', context)

# Register Page
def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.customer.first_name = form.cleaned_data.get('first_name')
        user.customer.last_name = form.cleaned_data.get('last_name')
        user.save()
        username = form.cleaned_data.get('username')
        print('username', username)
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render(request, 'property/register.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    if user.is_authenticated & user.is_staff:
        return render(request, 'property/dashboard.html')
    else:
        return redirect('property:login.html')

