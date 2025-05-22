from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Wheel, WheelItem
from .forms import WheelForm, WheelItemForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse

def home(request):
    wheels = Wheel.objects.all()
    return render(request, 'wheel/home.html', {'wheels': wheels})

@login_required
def create_wheel(request):
    if request.method == 'POST':
        wheel_form = WheelForm(request.POST)
        if wheel_form.is_valid():
            wheel = wheel_form.save(commit=False)
            wheel.user = request.user
            wheel.save()
            return redirect('wheel_detail', wheel_id=wheel.id)
    else:
        wheel_form = WheelForm()
    return render(request, 'wheel/create_wheel.html', {'form': wheel_form})

@login_required
def add_wheel_item(request, wheel_id):
    wheel = get_object_or_404(Wheel, id=wheel_id)
    if request.method == 'POST':
        form = WheelItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.wheel = wheel
            item.save()
            return JsonResponse({
                'status': 'success',
                'item': {
                    'id': item.id,
                    'text': item.text,
                    'weight': item.weight,
                    'color': item.color
                }
            })
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def show_data(request):
    user_wheels = Wheel.objects.filter(user=request.user)
    return render(request, 'wheel/show_data.html', {'wheels': user_wheels})

@login_required
def wheel_detail(request, wheel_id):
    wheel = get_object_or_404(Wheel, id=wheel_id)
    items = wheel.items.all()
    if request.method == 'POST':
        form = WheelItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.wheel = wheel
            item.save()
            return redirect('wheel_detail', wheel_id=wheel.id)
    else:
        form = WheelItemForm()
    return render(request, 'wheel/wheel_detail.html', {
        'wheel': wheel,
        'items': items,
        'form': form
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'wheel/register.html', {'form': form})