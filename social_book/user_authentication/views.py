from django.contrib.auth import logout
from . forms import BookForm
from datetime import datetime
from datetime import date
import re
from . models import Account, Books
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')

# login a user


def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_page')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')

# signup a user


def signup(request):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        x = request.POST['date_of_birth']
        public_visibility = request.POST.get('public_visibility')
        if public_visibility is None:
            public_visibility = False
        date_of_birth = datetime.strptime(x, '%Y-%m-%d')
        today = date.today()
        print(type(today), type(date_of_birth), 'todayyyyyy')
        age = today.year - date_of_birth.year - \
            ((today.month, today.day) < (date_of_birth. month, date_of_birth.day))
        if Account.objects.filter(email=email).exists():
            messages.error(request, 'Email account already exists!')
            return redirect('signup')
        if not re.match(pattern, email):
            messages.error(request, 'Please enter a valid email !')
            return redirect('signup')
        if password != confirm_password:
            messages.error(request, 'The password is incorrect !')
            return redirect(signup)
        Account.objects.create(
            email=email,
            username=username,
            birth_year=date_of_birth,
            age=age,
            public_visibility=public_visibility,
            password=make_password(password)
        )
        return render(request, 'login.html')

    return render(request, 'register.html')

# user page with user email


@login_required(login_url='/login/')
def user_page(request):
    user = request.user
    try:
        if request.method == 'POST':
            title = request.POST['title']
            author = request.POST['author']
            description = request.POST['description']
            price = request.POST['price']
            book = request.FILES['book']
            visibility = request.POST.get('visibility')
            if visibility is None:
                visibility = False
            Books.objects.create(
                title=title,
                author=author,
                description=description,
                price=price,
                book=book,
                visibility=visibility,
                user=user
            )
            print('save aaayii')
            return render(request, 'User.html', {'user': user})
        else:
            return render(request, 'User.html', {'user': user})
    except:
        return render(request, 'User.html', {'user': user})

# authors and sellers who is visible to public


def authors_and_sellers(request):
    users = Account.objects.filter(public_visibility=True)
    return render(request, 'AuthorsAndSellers.html', {'users': users})

# showing books of a user who is uploaded


@login_required(login_url='/login/')
def user_books(request):
    user = request.user
    books = Books.objects.filter(user=user)
    return render(request, 'UserBooks.html', {'books': books})

# logout a user


@login_required(login_url='/login/')
def Logout(request):
    logout(request)
    return redirect('login')
