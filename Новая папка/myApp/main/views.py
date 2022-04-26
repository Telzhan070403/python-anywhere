from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from main.forms import NewsForm
from main.models import News, SummerSport, WinterSport, Registration
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'main/home.html')


def insert(request):
    return render(request, 'main/insert.html')


def sut(request):
    return render(request, 'main/sutfood.html')


def flour(request):
    return render(request, 'main/flour.html')


def mens(request):
    return render(request, 'main/mens.html')


def sports(request):
    return render(request, 'main/sports.html')


def winter(request):
    sport = WinterSport.objects.all()
    return render(request, 'main/winter.html', {'sport': sport})


def summer(request):
    summer = SummerSport.objects.all()
    return render(request, 'main/Summer.html', {'summer': summer})


def womens(request):
    return render(request, 'main/womens.html')


def boots(request):
    return render(request, 'main/boots.html')


class NewsDeleteView(DeleteView):
    model = News
    success_url = '/news/'
    template_name = 'main/delete.html'


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'main/update.html'
    form_class = NewsForm


class NewsDetailView(DetailView):
    model = News
    template_name = 'main/details_view.html'
    context_object_name = 'news'


def insert(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news')
        else:
            error = 'Форма была неверной'

    form = NewsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/insert.html', data)


def news(request):
    new = News.objects.order_by('-id')
    return render(request, 'main/news.html', {'news': new})


# def registration(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('register_done')
#     else:
#         form = AddPostForm()
#     return render(request, 'main/register.html', {'form': form, 'title': 'registration'})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, ("There is some problem .. Try again.."))
            return redirect('login')
    else:
        return render(request, 'main/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('login')

# def sends_message(request):
#     send_mail("Web programming:back end","My content",
#               "2001033387@stu.sdu.edu.kz",
#               ["200103387@stu.sdu.edu.kz", "telzhanmuhadas@gmail.com"],
#               fail_silently=False, html_message="Хабарлама жиберилді")
#     return render(request, 'main/successfull.html')


# def sends_message(request):
#     email = EmailMessage(
#         'Hello', 'Body goes here', '2001033387@stu.sdu.edu.kz',
#         ['2001033387@stu.sdu.edu.kz', 'telzhanmuhadas@gmail.com', ],
#         headers={'Message-ID': 'foo'}, )
#     email.attach_file(r'C:\DJ\myApp\main\static\main\img\115.jpg')
#     email.send(fail_silently=False)
#     return render(request, 'main/successfull.html')


class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'main/susccessfull.html'

    def get(self, request):
        form = self.form_class()
        return render(request,'main/successfull.html',{'email_form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            files = request.FILES.getlist('attach')

            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, 'main/successfull.html',
                              {'email_form': form, 'error_message': 'Электрондық пошта мекенжайына жіберілді %s' % email})
            except:
                return render(request, 'main/successfull.html',
                              {'email_form': form, 'error_message': 'Не тіркеме тым үлкен немесе бүлінген'})

        return render(request, 'main/successfull.html',
                      {'email_form': form, 'error_message': 'Электрондық поштаны жіберу мүмкін емес. Тағы жасауды сәл кейінірек көріңізді өтінеміз'})