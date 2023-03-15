from django.shortcuts import render, redirect
from . forms import CadastroForm

# Create your views here.

"""_summary_
Se tiver apenas 1 elemento, então retorna 1 elemento, agora se tiver mais de 1 elemento, daí retorna 1 lista
Se for número no caso da idade, daí retorna un int
"""
def home(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if not form.is_valid():
            return render(request, 'index.html', {'form': form})
        return redirect('https://www.google.com')
    return render(request, 'index.html', {'form': CadastroForm()})
