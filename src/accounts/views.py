from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.generic import UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import SignUpForm

# @method_decorator(login_required, name='dispatch')
# class UserUpdateView(UpdateView):
#     model = User
#     fields = ('first_name', 'last_name', 'email')
#     template_name = 'accounts/my_account.html'
#     success_url = reverse_lazy('my_account')
#
#     def get_object(self):
#         return self.request.user

def signup(request):
    if request.method == 'POST':
        form  = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('boards:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
