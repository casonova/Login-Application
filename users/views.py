from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.contrib import messages
from django.views import View
from users.forms import LoginForm, SignupForm, UpdateForm


class HomeView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CustomLogoutView(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


class UpdateView(View):
    template_name = 'update.html'
    form_class = UpdateForm

    def get(self, request, *args, **kwargs):
        user_instance = request.user
        form = self.form_class(instance=user_instance)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        user_instance = request.user
        if request.method == "POST":
            form = self.form_class(request.POST, instance=user_instance)
            try:
                if form.is_valid():
                    password = form.cleaned_data.get('password')
                    confirm_password = form.cleaned_data.get('confirm_password')
                    if password == "" or confirm_password == "":
                        messages.error(request, 'Invalid Password')
                        return redirect('update')
                    if password and confirm_password and password != confirm_password:
                        messages.error(request, 'Password Does not match')
                        return redirect('update')
                    user_instance.set_password(password)
                    form.save()
                    return redirect('index')
            except PermissionDenied as e:
                return HttpResponseNotFound(f"Not found {e}")
            except Exception as e:
                return HttpResponseServerError(f"An error occurred: {e}")    
        form = self.form_class()    
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form = self.form_class(request.POST)
            try:
                if form.is_valid():
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')

                    user = authenticate(username=username, password=password)

                    if user is not None:
                        login(request,user)
                        return redirect('index')
                    else:
                        messages.error(request, "Invalid username or password")
                        return redirect('login')
                else:
                    messages.error(request, "Invalid form submission")
                    return render(request, 'login.html', {'form': form})
            except PermissionDenied as e:
                return HttpResponseNotFound(f"Not found {e}")
            except Exception as e:
                return HttpResponseServerError(f"An error occurred: {e}")
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

class SignupView(View):
    template_name = 'signup.html'
    form_class = SignupForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.form_class(request.POST)
            try:
                if form.is_valid():
                    email = form.cleaned_data.get('email')
                    first_name = form.cleaned_data.get('first_name')
                    last_name = form.cleaned_data.get('last_name')
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')
                    confirm_password = form.cleaned_data.get('confirm_password')

                    if password != confirm_password:
                        messages.error(request, 'Password Does not match')
                        return redirect('signup')
                    user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, username=username, password=password)
                    user.save()
                    return redirect('login')
                else:
                    messages.error(request, "Invalid Entry")
                    return redirect('signup')
            except PermissionDenied as e:
                return HttpResponseNotFound(f"Not found {e}")
            except Exception as e:
                return HttpResponseServerError(f"An error occurred: {e}")
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
