from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('login', login_view),
    path('register', register_view),
    path('logout', logout_view),
    path('llog', llog),
    path('profile/<int:id>', profile),
    path('ani/<int:id>', ani),
    path('getsearch', get_search),
    path('random', rand_m)
]
