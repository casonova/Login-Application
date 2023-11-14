from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.contrib.auth.models import User
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
        user_instance = request.user.profile
        if request.method == "POST":
            form = self.form_class(request.POST,request.FILES, instance=user_instance)
            try:
                if request.user.is_authenticated:
                    if form.is_valid():
                        form.save()
                        return redirect('index')
                    return render(request, self.template_name, {'form': form})
            except Exception as e:
                return HttpResponseServerError(f"An error occurred: {e} You should login first")    
        form = self.form_class(instance=request.user.profile)   
        full_name = user_instance.full_name 
        return render(request, self.template_name, {'form': form, 'full_name':full_name})
