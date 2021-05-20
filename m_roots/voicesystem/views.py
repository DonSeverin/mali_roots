from twilio.twiml.voice_response import VoiceResponse, Say, Gather
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, request

from .models import *


def index(request):
    context = {}
    return render(request, 'index.html', context)


def loginView(request):
    email = request.POST.get('email')
    password = request.POST.get('password1')

    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('/dashboard')

    context = {}
    return render(request, 'login.html', context)


def dashboard(request):
    tree = Tree.objects.all()
    user = User.objects.all()
    call = Call.objects.all()

    context = {'tree': tree, 'user': user, 'call': call}
    return render(request, 'dashboard.html', context)


def LogoutView(request):

    logout(request)
    return redirect('/login')


@csrf_exempt
def init_comm(request):
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()
    resp.say("Welcome to Mali Roots/Roots of Mali organization. Thank you for contacting us. This call could be recorded to improve our services.", voice='alice')# Welcome

    # Read a message aloud to the caller
    with resp.gather(num_digits=1, action='/engtreegather/') as g:
        g.say("For english, press 1. For French, press 2.", voice='alice') # Language Selection
        g.pause(length=1)

    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/answercall')

    return HttpResponse(str(resp), content_type='application/xml')


@csrf_exempt
def engtreegather(request):
    """Processes results from the <Gather> prompt in /voice"""
    # Start our TwiML response
    digits = request.POST.get('Digits', '')
    print(digits)
    resp = VoiceResponse()

    if digits == '1':
        resp.say('You selected english! Please select the following trees or seeds sighted, you can select multiple trees please press the # key when finished with selection. ')
        with resp.gather(finishOnKey="#", num_digits=5, action='/englocGather/') as g:
            g.say("For Pterocarpus erinaceus , press 1. For another tree, press 2., For another tree, press 3., For another tree, press 4., For another tree, press 5.", voice='alice') #List of trees 
    elif digits == '2':
        resp.say('You need support. We will help!')
    else:
        # If the caller didn't choose 1 or 2, apologize and ask them again
        resp.say("Sorry, I don't understand that choice.")

    # If the user didn't choose 1 or 2 (or anything), send them back to /voice
    resp.redirect('/answercall/')

    return HttpResponse(str(resp), content_type='application/xml')


@csrf_exempt
def englocGather(request):
    """Processes results from the <Gather> prompt in /voice"""
    # Start our TwiML response
    tree_digits = request.POST.get('Digits', '')
    resp = VoiceResponse()

    if tree_digits == '0':
        resp.say('No Trees selected. ')
        resp.redirect('/#/')
    elif tree_digits >= '1':
        resp.say('Your selection has been confirmed, Thank You!')
        with resp.gather(num_digits=6, action='/engconGather/') as g:
            g.say("Please specify the area code where the trees have been sighted", voice='alice') #List of tree
    else:
        # If the caller didn't choose 1 or 2, apologize and ask them again
        resp.say("Sorry, I don't understand that choice.")

    # If the user didn't choose 1 or 2 (or anything), send them back to /voice
    resp.redirect('/answercall/')

    return HttpResponse(str(resp), content_type='application/xml')


@csrf_exempt
def engconGather(request):
    """Processes results from the <Gather> prompt in /voice"""
    # Start our TwiML response
    tree_digits = request.POST.get('Digits', '')
    resp = VoiceResponse()

    if tree_digits == '0':
        resp.say('No Trees. ')
    elif tree_digits >= '1':
        resp.say('Your selection has been confirmed, Thank You!')
        with resp.gather(num_digits=1, action='/engconfirmGather/') as g:
            g.say("Can we contact you for further information? If no option is selected the message will be replayed once. For Yes press 1. For No press 2.") #List of tree
    else:
        # If the caller didn't choose 1 or 2, apologize and ask them again
        resp.say("Sorry, I don't understand that choice.")

    # If the user didn't choose 1 or 2 (or anything), send them back to /voice
    resp.redirect('/answercall/')

    return HttpResponse(str(resp), content_type='application/xml')


@csrf_exempt
def engconfirmGather(request):
    """Processes results from the <Gather> prompt in /voice"""
    # Start our TwiML response
    tree_digits = request.POST.get('Digits', '')
    resp = VoiceResponse()

    if tree_digits == '1':
        resp.say('You have successfully registered the sighting. Thank you for your contribution.You may now dissconnect the call')
    elif tree_digits >= '1':
        resp.say('Thank you for your contribution! You may now dissconnect the call')
    else:
        # If the caller didn't choose 1 or 2, apologize and ask them again
        resp.say("Sorry, I don't understand that choice.")

    return HttpResponse(str(resp), content_type='application/xml')