from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

from .forms import SignUpForm
# Create your views here.
def home(request):

    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))

def thankyou(request):

    form - SignUpForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        # commmet
        subject = "Thank for your Pre-Order from Jaythaceo"
        message = "Welcome to jaythaceo.com We very much appreciate your business./n We will be in touch soon"
        from_email = settings.EMAIL_HOST_USER
        to_list - [save_it.email, settings.EMAIL_HOST_USER]

        send.mail(subject, message, from_email, to_list, fail_silently=True)

        messages.success(request, "Thank you for your order. We will be in touch")
        return HttpResponseRedirect('/thank-you/')

    return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))

def aboutus(request):
    return render_to_response("aboutus.html",
                              locals(),
                              context_instance=RequestContext(request))
