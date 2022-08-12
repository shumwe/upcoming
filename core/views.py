from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from core.forms import MailingSignUpForm

def home(request):
    if request.method == 'POST':
        subscribe_form = MailingSignUpForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            messages.success(request, 'Your email was submitted succesfully')
            return HttpResponseRedirect("")
        else:
            messages.error(request, 'An error occured when submitting your email. Please try again.')
    else:
        subscribe_form = MailingSignUpForm()
    context = {'subscribe_form': subscribe_form}
    return render (request, 'core/index.html', context)