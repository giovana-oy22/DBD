from django.shortcuts import render, redirect
from .forms import ProdutoForm
from .models import Produto

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # volta pra página inicial
    else:
        form = ProdutoForm()

    return render(request, 'adicionar_produto.html', {'form': form})

def listar_produtos(request):
    query = request.GET.get('q')
    produtos = Produto.objects.all()

    # 🔍 busca opcional
    if query:
        produtos = produtos.filter(nome__icontains=query)

    return render(request, 'core/lista.html', {
        'produtos': produtos,
        'query': query
    })