from django.shortcuts import render, redirect
from app.forms import ClienteForm, AgendamentoForm, OrcamentoForm
from app.models import Cliente

# Create your views here.
def home(request):
    return render(request, 'index.html')


def form(request):
    data = {}
    data['form'] = ClienteForm()
    return render(request, 'form.html', data)

def create(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def read(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Cliente.objects.filter(nome__icontains=search)
    else:
        data['db'] = Cliente.objects.all()
    return render(request, 'read.html', data)

def view(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    data['form'] = ClienteForm(instance=data['db'])
    return render(request, 'read.html', data)

def update(request, pk):
    data ={}
    data['db'] = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Cliente.objects.get(pk=pk)
    db.delete()
    return redirect('read')

def agendamento(request):
    data = {}
    data['form'] = AgendamentoForm()
    return render(request, 'agendamento.html', data)

def orcamento(request):
    data = {}
    data['form'] = OrcamentoForm()
    return render(request, 'orcamento.html', data)