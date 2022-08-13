from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

@login_required
def profile(request):
    user = request.user
    #TODO: add more context
    context = {
        'user': user
        }
    return render(request, 'accounts/profile.html', context)