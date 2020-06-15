from django.shortcuts import render,redirect
from django.core.mail import BadHeaderError, send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from ButterflyApp.form import SignUpForm
from django.contrib.sessions.backends.db import SessionStore
from datetime import datetime
from ButterflyApp.models import GeneralKnowledge
import math
from django.http import HttpResponse


# Create your views here.
def index(request):
    year = datetime.now().year
    request.session['year'] = year
    return render(request,'ButterflyApp/index.html')

@login_required
def about(request):
    request.session['logged_in'] = 1
    return render(request,'ButterflyApp/about.html')

@login_required
def english(request):
    request.session['logged_in'] = 1
    return render(request,'ButterflyApp/english.html')

@login_required
def contact_us(request):
    request.session['logged_in'] = 1
    if request.method == 'POST':
        name = 'Hello, My name is ' + request.POST['name'] + '.'
        from_email = 'This is my email ' + request.POST['email']
        if request.POST['phone']:
            phone = ' and mobile number ' + request.POST['phone'] + '. '
        else:
            phone = '. '
        message = request.POST['message']
        subject = 'Mail From ' + request.POST['name']
        message = name + from_email + phone + message
        receiver_message = 'Hey ' + request.POST['name'] + ',' + ' We get\'s your mail and will contact you as soon as possible. Enjoy ! '
        try:
            send_mail(subject, message,'from', ['to'])
            send_mail('Thanks for contacting us', receiver_message,'from', ['to'])
            return render(request,'ButterflyApp/thank_you.html')
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    return render(request,'ButterflyApp/contact_form.html')

@login_required
def mathematics(request):
    request.session['logged_in'] = 1
    return render(request,'ButterflyApp/mathematics.html')

@login_required
def hindi(request):
    request.session['logged_in'] = 1
    return render(request,'ButterflyApp/hindi.html')

def cart_system(request):
    if request.POST.get('item') and request.POST.get('quantity'):
        if request.session.get('basket'):
            if request.session.get('count'):
                count = request.session['count']
                count = count + 1
                item_dict = dict()
                item_dict['item'] = request.POST['item']
                item_dict['quantity'] = request.POST['quantity']
                request.session['basket'].update({count:item_dict})
                request.session['count'] = count

        else:
            count = 1
            request.session['count'] = count
            request.session['basket'] = dict()
            item_dict = dict()
            item_dict['item'] = request.POST['item']
            item_dict['quantity'] = request.POST['quantity']
            request.session['basket'].update({count:item_dict})
        print(request.session['basket'])
        return render(request,'ButterflyApp/display_products.html')
    return render(request,'ButterflyApp/add_item.html')

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'registration/signup.html',{'form':form})

def logout(request):
    return render(request,'registration/logout.html')

def general_knowledge(request):
    if request.GET.get('page_no',1):
        # start_index = (int(request.GET.get('page_no',1)) - 1)*5
        flag = 0
        page_count = int(request.GET.get('page_no',1))
        count = GeneralKnowledge.objects.all().count()
        max_page_count = math.ceil(count/5)
        if (page_count <= max_page_count) and ((page_count + 1) <= max_page_count):
            page_count = request.GET.get('page_no',1)
            flag = 1

        start_index = (int(page_count) - 1)*5
        end_index = 5*int(request.GET.get('page_no',1))
        gk_qs = GeneralKnowledge.objects.all()[start_index:end_index]
        question_list = []
        if gk_qs and len(gk_qs):
            for i in gk_qs:
                context = dict()
                context['question'] = i.question
                context['answer'] = i.answer
                question_list.append(context)
        if flag:
            return render(request,'ButterflyApp/general_knowledge.html',{'que_data':question_list,'page_count':page_count})
        return render(request,'ButterflyApp/general_knowledge.html',{'que_data':question_list,'pre_page_count':page_count})

def quiz(request):
    return HttpResponse("<center><h2 style='color:orange;'>This page is under construction !!!</h2><hr></center>")

def games(request):
    return HttpResponse("<center><h2 style='color:orange;'>This page is under construction !!!</h2><hr></center>")
