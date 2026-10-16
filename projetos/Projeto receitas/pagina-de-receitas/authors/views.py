from django.shortcuts import render, redirect

from .forms import RegisterForm

from django.http import Http404

def register_view(request):
    form = RegisterForm()
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })
    
def register_create(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    form = RegisterForm(POST)

    if not form.is_valid():
        return render(request, 'authors/pages/register_view.html', {
            'form': form,
        })
    
    return redirect('authors:register')
