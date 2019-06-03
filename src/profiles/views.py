from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import Profile
from .forms import ProfileForm, UserForm

@method_decorator(login_required, name='dispatch')
class ProfileListView(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'profiles/profile.html'

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profiles:update_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/photo_list.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


# def photo_list(request):
#     photos = Photo.objects.all()
#     if request.method == 'POST':
#         form = PhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('photo_list')
#     else:
#         form = PhotoForm()
#     return render(request, 'profiles/photo_list.html', {'form': form, 'photos': photos})
