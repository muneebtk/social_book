from . models import Books
from django.shortcuts import redirect


# decorator for checking if the user has uploaded books
def book_exist(view_func, redirect_url='user_page'):
    def wrapper(request):
        if Books.objects.filter(user=request.user).exists():
            return view_func(request)
        return redirect(redirect_url)
    return wrapper

# authentication not required decorator

def authentication_not_required(view_func, redirect_url='user_page'):
    def wrapper(request):
        if not request.user.is_authenticated:
            return view_func(request)
        return redirect(redirect_url)
    return wrapper

