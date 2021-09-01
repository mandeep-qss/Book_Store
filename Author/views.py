from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect , JsonResponse
from Author.models import User
from django.contrib import messages
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from Author.forms import FormUser
from Author.tokens import account_activation_token
from django.contrib.auth import login
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from Author.forms import FormUser,UserInputForm




# Create your views here.

def signupView(request):
    if 'signup' in request.POST:
        f = request.POST['sfirstname']
        l = request.POST['slastname']
        e = request.POST['semail']
        ps = request.POST['password']
        data = User(first_name = f , last_name= l , email = e , password = ps)
        data.save()
        # Email
        current_site = get_current_site(request)
        subject = 'Activate Your Account'
        message = render_to_string('account_activation_email.html', {
            'user': data,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(data.pk)),
            'token': account_activation_token.make_token(data),
        })
        em = EmailMessage(subject,message,to=[e])
        em.send()
        return redirect('account_activation_sent')
    # else:
    #     signupView()   
    getData = User.objects.all()
    return render(request, 'signup.html', {'data':getData})





def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        # user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('login')
    else:
        return render(request, 'account_activation_invalid.html')





def account_activation_sent(request):
    return render(request,'account_activation_sent.html')





def loginView(request):
    if 'logg' in request.POST:
        e = request.POST['emaill']
        ps = request.POST['passwordd']
        user = authenticate(email = e , password = ps)		
        obj = User.objects.get(email=e)
        if user is not None and user.is_active:
            login(request,user)
            messages.add_message(request,messages.INFO,'Login Successfullyy')
            resp = HttpResponseRedirect('../home')
            resp.set_cookie('user_id',user.id)
            resp.set_cookie('user_email',user.email)
            return resp
        elif obj.get_isActiveStatus() == False:
            messages.add_message(request,messages.INFO,'User is not active')
            resp = HttpResponseRedirect('../signup')
            return resp
        elif obj.get_isActiveStatus() == True:
            messages.add_message(request,messages.INFO,'Your password is incorrect!!')
            resp = HttpResponseRedirect('../login')
            return resp
        else:
            messages.add_message(request,messages.INFO,'You are not registered!!')
            return HttpResponseRedirect('../mm')
            return resp
    else:
        formvalue = UserInputForm
        return render(request,'login.html',{'formvalue':formvalue})
