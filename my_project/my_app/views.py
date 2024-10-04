from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


from django.http import HttpResponse

response = '''
    <html>
        <body>
            <p>hurryyy!!!! you are Sign up successfully!</p>
            <p>login to explore our diverse online courses</p>
            <a href="/login">
                <button>Login</button>
            </a>
        </body>
    </html>
'''

from django.contrib.auth.models import User
from .forms import SignUpForm 

def index(request):
    return render (request ,"index.html")

def course(request):
    return render (request ,"course.html")

def course_xe(request):
    return render (request ,"course_xe.html")

def about(request):
    return render (request ,"about.html")    

def help(request):
    return render (request ,"help.html") 

@login_required
def home(request):
    return render (request ,"home.html")

def sign_in(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('user_name')
            first_name = form.cleaned_data.get('first_name') 
            last_name = form.cleaned_data.get('last_name') 
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            try:
                my_user = User.objects.create_user(username=uname,first_name=first_name,last_name=last_name, email=email, password=password)
                my_user.save()
                return HttpResponse(response)
            except Exception as e:
                form.add_error(None, f"Error creating user: {e}")

    else:
        form = SignUpForm()

    return render(request, 'sign_in.html', {'form': form})


def login_view(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to the homepage or dashboard if logged in

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's built-in authentication method
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log in the user
            return redirect('home')  # Redirect to the homepage or dashboard
        
        else:
            # If authentication fails, return to login page with an error
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    # If it's a GET request, render the login form
    return render(request, 'login.html')

from django.contrib.auth import logout

# @require_POST
def logout_view(request):
    logout(request)
    return redirect('index') 

@login_required
def account_view(request):
    return render(request, 'account.html')

# def back(request):
#     return render (request ,"papa.html")

