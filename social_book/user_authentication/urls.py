from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('user/', views.user_page, name='user_page'),
    path('authors_and_sellers/', views.authors_and_sellers,
         name='authors_and_sellers'),
    path('books/', views.user_books, name='user_books'),
    path('logout/', views.Logout, name='logout'),

]
