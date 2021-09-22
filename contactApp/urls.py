from django.urls import path
from .import views
from django.urls.resolvers import URLPattern


urlpatterns = [
     path('', views.home, name='home'),
      path('accounts/login/', views.login_view, name='login'),
     path('logout', views.logout_view),
     path('home', views.home),
     path('add', views.createView, name='add'),
     path('addcontact', views.addcontact),
     path('update', views.updateView, name='update'),
     path('display', views.displayView, name='display'),
     path('delete', views.deleteView, name='delete'),
    

     path('deletecontact', views.deleteContact),
     path('displaycontacts', views.displayContact),
     path('updatename', views.updateName),
     path('updatenumber', views.updateNumber),
     path('updateaddress',views.updateAddress)


     
]