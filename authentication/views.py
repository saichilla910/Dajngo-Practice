from django.shortcuts import render
from .forms import Register_form
from django.shortcuts import redirect
from django.contrib import messages 
from django.contrib.auth import logout
# Create your views here.
def register(request):
    if request.method == "POST":
        form = Register_form(request.POST)
        print(form.errors)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'ACCOUNT Created successfully for {username}')
            return redirect('login')
    else:
        form = Register_form()

    return render(request, 'auth/register.html', {'form': form})

def login(request):
    return render(request,'auth/login.html')
def logout_user(request):
    logout(request)
    return render(request,'auth/logout.html')