from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistroFormulario, ProfileForm
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def registro(req):
    if req.method == 'POST':
        form = RegistroFormulario(req.POST)
        if form.is_valid():
            user = form.save()
            login =(req, user)
            return redirect('index')
    else:
        form = RegistroFormulario()
    return render(req, 'registro/registro.html', {'form': form})

def login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                return redirect(request.GET.get('next', 'profile')) 
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Formulario inválido. Revisa los datos.")
    return render(request, 'registro/login.html', {'form': form})

def logout_view(req):
    logout(req)
    return redirect('index')

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile') 
    else:
        form = ProfileForm(instance=user)

    return render(request, 'registro/profile.html', {'form': form})

#@permission_required('usuarios.cam_scrum', raise_exception=True)
#def vista_scrum(req):
#    return render(req, 'scrum.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile') 
    else:
        form = ProfileForm(instance=request.user)
    
    return render(request, 'registro/edit_profile.html', {'form': form})

@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user) 
        if form.is_valid():
            form.save() 
            return redirect('profile') 
    else:
        form = ProfileForm(instance=user)
    
    return render(request, 'registro/profile.html', {'form': form})


def is_scrum_user(user):
    return user.groups.filter(name='crud user').exists()

#@user_passes_test(is_scrum_user)
#def vista_scrum(req):
#    return render(req, 'scrum.html')