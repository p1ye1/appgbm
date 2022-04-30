from msilib.schema import Class
from django.shortcuts import render, redirect
from .models import Planes, Usuarios_register, Comentarios_inicio
from django.db.models import Q
from .forms import PersonasForm, ComentaForm, RegisterForm, userForm, loginForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView

# Create your views here.
def inicio(request):
    plan = Planes.objects.all()
    comment = Comentarios_inicio.objects.all()
    datos = {
        "principal":plan,
        "form":PersonasForm,
        "formComenta":ComentaForm,
        "comentario":comment
    }
    if request.method == 'POST':
        formulario = PersonasForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            datos["form"] = formulario

    if request.method == 'POST':
        formutario = ComentaForm(data=request.POST)
        if formutario.is_valid():
            formutario.save()
        else:
            datos["formComenta"] = formutario
    return render(request, 'app/inicio.html', datos)

def base(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    post = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset)
        ).distinct()
    datosbase = {
        "form":PersonasForm
    }
    if request.method == 'POST':
        formulario = PersonasForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            datosbase["form"] = formulario
    return render(request, 'app/base.html', datosbase)

def galeria(request):
    return render(request, 'app/pages/gallery.html')
def full(request):
    return render(request, 'app/pages/full-width.html')
def sidebar_l(request):
    return render(request, 'app/pages/sidebar-left.html')
def sidebar_r(request):
    return render(request, 'app/pages/sidebar-right.html')
def basic(request):
    return render(request, 'app/pages/basic-grid.html')
def icons(request):
    return render(request, 'app/pages/font-icons.html')
def buscar(request):
    if request.GET['busqueda']:
        query = request.GET['busqueda']
        planes = Planes.objects.filter(titulo__icontains=query)
        datos = {
        "planes": planes,
        "query" : query
        }
        return render(request, 'app/pages/buscar.html',datos)
    else:
        return render(request, 'app/pages/buscar.html')
def login(request):
    return render(request, 'app/login.html')
def logout(request):
    return render(request, 'app/logout.html')
def register(request):
    registrar = Usuarios_register.objects.all()
    datos = {
        "register":registrar
    }
    if request.method == 'POST':
        formulario = RegisterForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            datos["formRegis"] = formulario
    return render(request, 'app/register.html', datos)



class Registro(View):
  form_class = userForm
  initial = {'key': 'value'}
  template_name = 'app/pages/register.html'

  def get(self, request, *args, **kwargs):
    form = self.form_class(initial=self.initial)
    return render(request, self.template_name, {'form': form})

  def post(self, request, *args, **kwargs): 
    form = self.form_class(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account created for {username}')
        return redirect(to='/')
    return render(request, self.template_name, {'form': form})
  def dispatch(self, request, *args, **kwargs):
    # will redirect to the home page if a user tries to access the register page while logged in
    if request.user.is_authenticated:
        return redirect(to='/')
    # else process dispatch as it otherwise normally would
    return super(Registro, self).dispatch(request, *args, **kwargs)




class CustomLoginView(LoginView):
  form_class = loginForm
  def form_valid(self, form):
    remember_me = form.cleaned_data.get('remember_me')
    if not remember_me:
        # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
        self.request.session.set_expiry(0)
        # Set session as modified to force data updates/cookie to be saved.
        self.request.session.modified = True
    # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
    return super(CustomLoginView, self).form_valid(form)

