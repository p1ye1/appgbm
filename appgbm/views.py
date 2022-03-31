from operator import index
from django.shortcuts import render
from .models import Planes
from django.db.models import Q
from .forms import PersonasForm

# Create your views here.
def index(request):
    plan = Planes.objects.all()
    datos = {
        "principal":plan,
        "form":PersonasForm
    }
    if request.method == 'POST':
        formulario = PersonasForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            datos["form"] = formulario
    return render(request, 'app/index.html', datos)

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
    if request.GET['buscar']:
        query = request.GET['buscar']
        plan = Planes.objects.filter(titulo__icontains=query).order_by('-ubicacion')
        datos = {
            "principal" : plan,
            "query" : query
        }
        return render(request, 'app/buscar.html', datos)
    else:
        return render(request, 'app/buscar.html')

