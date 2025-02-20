from django.shortcuts import render,redirect
from django.views import View

class Landing(View):
    def get(self,request):
        return render(request,"Landing.html")

from .forms import Reg_form

class Staff(View):
    template_name = 'Staff_Reg.html'
    form_class = Reg_form

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('Login')  # Adjust 'Login' to the actual URL or name for your login page

        return render(request, self.template_name, {'form': form})

from django.contrib.auth import authenticate, login

class Login_page(View):
    template_name = 'Login_page.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'Username OR Password incorrect')

        context = {}
        return render(request, self.template_name, context)

class Home(View):
    def get(self,request):
        return render(request, 'Home_page.html')
    
class Team(View):
    def get(self,request):
        return render(request, 'Team.html')

from django.contrib.auth import logout

class LogoutPage(View):
    def get(self, request):
        logout(request)
        return redirect('Land')


from django.shortcuts import render, redirect
from django.views import View
from .forms import user_personal_form
from .models import user_personal_model

class StudentInfo(View):
    template_name = 'Student_Info.html'
    success_template_name = 'Home_page.html'
    form_class = user_personal_form

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})
        else:
            # Redirect to the login page or handle unauthenticated users.
            return redirect('Login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            if user_personal_model.objects.filter(user=user, registration_flag=False).exists():
                messages.warning(request, 'You are already registered.')
                return render(request, self.template_name)
            else:
                form.instance.user = user
                form.save()
                user_personal_model.objects.filter(user=user).update(registration_flag=False)
                messages.success(request, 'Registration successful!')
                return render(request, self.success_template_name, {'form': form})
        else:
            messages.error(request, 'Form submission failed. Please check your inputs.')
            return render(request, self.template_name, {'form': form})

    
from .models import  user_personal_model

class StudentData(View):
    template_name = 'Student_Data.html'

    def get(self, request, *args, **kwargs):
        models = user_personal_model.objects.all()
        return render(request, self.template_name, {'models': models})

from django.contrib import messages
from .forms import staff_personal_form
from .models import staff_database

class StaffInfo(View):
    template_name = 'Staff_info.html'
    form_class = staff_personal_form

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})
        else:
            return redirect('Login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            if staff_database.objects.filter(user=request.user, registration_flag=False).exists():
                messages.error(request, 'You have already submitted your information.')
                return render(request, self.template_name)
            else:
                form.instance.user = user
                form.save()
                staff_database.objects.filter(user=user).update(registration_flag=False)
                messages.success(request, 'Information submitted successfully.')
                return render(request, self.template_name, {'form': form})
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
        return render(request, self.template_name, {'form': form})
    
from .models import  staff_database

class StaffData(View):
    template_name = 'Staff_data.html'

    def get(self, request, *args, **kwargs):
        models = staff_database.objects.all()
        return render(request, self.template_name, {'models': models})
