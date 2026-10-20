from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model

from .models import Profile, Tariff


def home(request):
    return render(request, "taxi/home.html")

@login_required
def passenger_dashboard(request):
    is_passenger = Profile.objects.filter(
        user=request.user,
        role=Profile.Role.PASSENGER,
    ).exists()

    if request.user.is_staff or not is_passenger:
        raise PermissionDenied

    tariffs = Tariff.objects.filter(is_active=True)

    context = {
        'tariffs': tariffs,
    }

    return render(request, "taxi/passenger_dashboard.html", context)

@login_required
def dashboard(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')

    profile = Profile.objects.filter(user=request.user).first()

    if profile is None:
        raise PermissionDenied('Для пользователя не создан профиль')

    if profile.role == Profile.Role.PASSENGER:
        return redirect('passenger_dashboard')
    
    if profile.role == Profile.Role.DRIVER:
        return redirect('driver_dashboard')
    
    return redirect('home')

@login_required
def driver_dashboard(request):
    is_driver = Profile.objects.filter(
        user=request.user,
        role=Profile.Role.DRIVER,
    ).exists()

    if request.user.is_staff or not is_driver:
        raise PermissionDenied

    return render(request, 'taxi/driver_dashboard.html')

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        raise PermissionDenied

    User = get_user_model()

    users_count = User.objects.count()

    passenger_count = Profile.objects.filter(
        role=Profile.Role.PASSENGER,
    ).count()
    
    driver_count = Profile.objects.filter(
        role=Profile.Role.DRIVER,
    ).count()

    context = {
        'user_count': users_count,
        'passenger_count': passenger_count,
        'driver_count': driver_count
    }

    return render(
        request,
        'taxi/admin_dashboard.html',
        context,
    )