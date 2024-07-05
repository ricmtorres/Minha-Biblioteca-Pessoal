from django.shortcuts import render, redirect
from .models import Usuario, Livro
from django.http import HttpResponse


def registro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        Usuario.objects.create(nome=nome, senha=senha)
    return render(request, 'biblioteca/registro.html')


def login(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        try:

            usuario = Usuario.objects.get(nome=nome, senha=senha)
            print(f'{usuario.nome} --> {usuario.id}')
            request.session['usuario_id'] = usuario.id

            return redirect('dashboard')
        except Usuario.DoesNotExist:
            return HttpResponse('Nome de usuário ou senha inválidos')
    return render(request, 'biblioteca/login.html')


def adicionar_livro(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        usuario = Usuario.objects.get(id=usuario_id)
        if request.method == 'POST':
            titulo = request.POST.get('titulo')
            autor = request.POST.get('autor')
            ano_publicacao = request.POST.get('ano_publicacao')
            livro = Livro(titulo=titulo, autor=autor, ano_publicacao=ano_publicacao, usuario=usuario)
            livro.save()
            return redirect('dashboard')
        return render(request, 'biblioteca/adicionar_livro.html')
    return redirect('login')


def personalizar(request):
    if request.method == 'POST':
        cor_preferida = request.POST.get('cor_preferida')
        if cor_preferida:
            request.session['cor_preferida'] = cor_preferida
            response = redirect('dashboard')
            response.set_cookie('cor_preferida', cor_preferida, max_age=3600)
            return response
        else:
            return render(request, 'usuarios/personalizar.html', {'error': 'Por favor, selecione uma cor preferida.'})
    else:
        return render(request, 'biblioteca/personalizar.html')


def dashboard(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    usuario = Usuario.objects.get(id=usuario_id)
    livros = Livro.objects.filter(usuario=usuario)  # Obtendo os livros do usuário
    cor_preferida = request.COOKIES.get('cor_preferida', 'default')
    return render(request, 'biblioteca/dashboard.html', {
        'usuario': usuario,
        'livros': livros,
        'cor_preferida': cor_preferida
    })


def logout(request):
    request.session.flush()
    response = redirect('login')
    response.delete_cookie('cor_preferida')
    return response
