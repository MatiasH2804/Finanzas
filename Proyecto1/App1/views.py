from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ingreso, Gasto, Categoria
from .forms import SueldoFormulario, GastoFormulario, CategoriaFormulario

@login_required
def inicio(request):
    return render(request, "App1/index.html")

@login_required
def calculos(request):
    if request.method == "POST":
        ingreso_formulario = SueldoFormulario(request.POST)
        gasto_formulario = GastoFormulario(request.POST)
        
        if ingreso_formulario.is_valid():
            ingreso = ingreso_formulario.save(commit=False)
            ingreso.usuario = request.user
            ingreso.save()
            return redirect('resumen')
        
        if gasto_formulario.is_valid():
            gasto = gasto_formulario.save(commit=False)
            gasto.usuario = request.user
            gasto.save()
            return redirect('resumen')
    else:
        ingreso_formulario = SueldoFormulario()
        gasto_formulario = GastoFormulario()

    return render(request, "App1/calculos.html", {
        "ingreso_formulario": ingreso_formulario,
        "gasto_formulario": gasto_formulario
    })

@login_required
def historial(request):
    ingresos = Ingreso.objects.filter(usuario=request.user)
    gastos = Gasto.objects.filter(usuario=request.user)
    return render(request, "App1/historial.html", {
        "ingresos": ingresos,
        "gastos": gastos
    })

@login_required
def categorias(request):
    if request.method == "POST":
        categoria_formulario = CategoriaFormulario(request.POST)
        
        if categoria_formulario.is_valid():
            categoria_formulario.save()
            return redirect('categorias')
    else:
        categoria_formulario = CategoriaFormulario()

    categorias = Categoria.objects.all()
    return render(request, "App1/categorias.html", {
        "categoria_formulario": categoria_formulario,
        "categorias": categorias
    })

@login_required
def resumen(request):
    ingresos = Ingreso.objects.filter(usuario=request.user)
    gastos = Gasto.objects.filter(usuario=request.user)
    total_ingresos = sum(ingreso.cantidad for ingreso in ingresos)
    total_gastos = sum(gasto.cantidad for gasto in gastos)
    saldo_restante = total_ingresos - total_gastos

    return render(request, "App1/resumen.html", {
        "total_ingresos": total_ingresos,
        "total_gastos": total_gastos,
        "saldo_restante": saldo_restante
    })

@login_required
def configuracion(request):
    return render(request, "App1/configuracion.html")
