from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseServerError, Http404
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from .forms import ProfileForm
from django.views import View


class ProfileView(View):
    template_name = 'profile.html'
    form_class = ProfileForm

    def get(self, request, *args, **kwargs):
        user_instance = request.user.profile
        full_name = user_instance.full_name
        form = self.form_class(instance=user_instance)
        return render(request, self.template_name, {'form': form, 'full_name':full_name})

    def post(self, request, *args, **kwargs):
        user_profile = request.user.profile
        try:
            user_instance = get_object_or_404(User, profile = user_profile)
            print(user_instance)
            if request.method == "POST":
                form = self.form_class(request.POST,request.FILES, instance=user_instance)

                if request.user.is_authenticated:
                    if form.is_valid():
                        form.save()
                        return redirect('index')
                    return render(request, self.template_name, {'form': form})
                return HttpResponseServerError("You should login first") 
        except Exception as e:
            return Http404(f"An error occurred: {e} ")    
        form = self.form_class(instance=user_instance)   
        full_name = user_instance.full_name 
        return render(request, self.template_name, {'form': form, 'full_name':full_name})
