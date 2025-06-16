from django.urls import path
from . import views

# TODO add an app_name
app_name = "timenye.core"
urlpatterns = [
    # TODO add names to the urls
    path('', views.index),
    path('discover/', views.for_you),
    path('for-you/', views.for_you),
    path('login/', views.login),
    path('signup/', views.signup),
    path('sport/<sport_name>', views.sport_home),
    path('sports/', views.sports),
    path('teams/', views.teams),

]
