from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterationForm
from django.contrib import messages

# Create your views here.

class RegisterView(View):
    template_name = 'accounts/registeration/register.html'
    form_class = RegisterationForm
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'form': kwargs.get('form') or self.form_class()
        })
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            messages.success(request, 'Account created successfully :)')
            if user.is_active:
                login(request, user)
                
            messages.warning(request, 'To login, You need to activate your email first')
            return redirect('all_products')
        else:
            return self.get(request=request, form=form)

class LoginView(View):
    template_name = 'accounts/registeration/login.html'
    form_class = LoginForm
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'form': kwargs.get('form') or self.form_class()
        })
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            login(request, form.user)
            messages.info(request, 'You are logged in now!')
            return redirect('all_products')
        return self.get(request, form=form)