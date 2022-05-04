from django.shortcuts import render, redirect
from .models import *
from .forms import NewsForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import UpdateView
from rest_framework import generics
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {from_email}', message,
                          '200103169@stu.sdu.edu.kz',
                          ['yeralyadilet@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "main/sendMessage.html", {'form': form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
    context = {}
    return render(request, "main/login.html", context)


def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')


class NewsDeleteView(DeleteView):
    model = Module1
    success_url = '/'
    template_name = 'main/delete.html'


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'main/insert.html', {
        'form': form
    })


class NewsUpdateView(UpdateView):
    model = Module1
    template_name = 'main/update.html'
    form_class = NewsForm


class NewsDetailView(DetailView):
    model = Module1
    template_name = 'main/details_view.html'
    context_object_name = 'news'


def insert(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверной'

    form = NewsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/insert.html', data)


def news(request):
    new = Module1.objects.order_by('-id')
    return render(request, 'main/news.html', {'news': new})
