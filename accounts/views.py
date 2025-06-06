from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import FarmerRegistrationForm, FarmForm, FarmerLoginForm
from .models import FarmerProfile, Farm


def user_register(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            profile = FarmerProfile.objects.get(user=user)
            if profile.role == 'farmer':
                return redirect('add_farm')
            elif profile.role == 'agronomist':
                return redirect('agronomist_dashboard')
            elif profile.role == 'extension officer':
                return redirect('extension_officer_dashboard')
    else:
        form = FarmerRegistrationForm()
    return render(request, 'accounts/farmer_register.html', {'form': form})

def add_farm(request):
    farmer_profile = FarmerProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = FarmForm(request.POST)
        if form.is_valid():
            farm = form.save(commit=False)
            farm.farmer = farmer_profile
            farm.save()
            if 'add_another' in request.POST:
                return redirect('add_farm')
            else:
                return redirect('farmer_dashboard') 
    else:
        form = FarmForm()
    return render(request, 'accounts/add_farm.html', {'form': form})




@login_required
def farmer_dashboard(request):
    farmer_profile = FarmerProfile.objects.get(user=request.user)
    farms = Farm.objects.filter(farmer=farmer_profile)
    # You can add more context data as needed
    return render(request, 'accounts/farmer_dashboard.html', {
        'farmer_profile': farmer_profile,
        'farms': farms,
    })


login_required
def agronomist_dashboard(request):
    return render(request, 'accounts/agronomist_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'accounts/extension_officer_dashboard.html')


def farmer_login(request):
    if request.method == 'POST':
        form = FarmerLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect based on role
            profile = user.farmerprofile
            if profile.role == 'farmer':
                return redirect('farmer_dashboard')
            elif profile.role == 'agronomist':
                return redirect('agronomist_dashboard')
            elif profile.role == 'extension officer':
                return redirect('extension_officer_dashboard')
    else:
        form = FarmerLoginForm()
    return render(request, 'accounts/farmer_login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')