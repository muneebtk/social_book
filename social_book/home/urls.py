from django.urls import path, include
from . import views
urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.authtoken')),
    path('all_books/', views.all_books),
    # path('alchemy/', views.alchemy),
]
