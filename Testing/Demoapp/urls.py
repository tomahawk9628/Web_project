from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [ 
    #path('', views.hi, name='home-page'),
    #path('', views.hel, name='hel'),
    #path('',views.post_list,name='post_list'),
    #path('',views.disp,name='index'),
    path('',views.home,name='home'),
    path('login/',views.login_url,name='login_url'),
    path('register/',views.register,name='register'),
    path('dashboard/',views.dashboardView,name='dashboard'),
    path('logout/',LogoutView.as_view(next_page='login_url'),name='logout'),
    path('adminlogin/',views.adlog,name='adlog'),
    path('adminl/',views.adminl,name='adminl'),
    path('<int:movie_id>/',views.mdetails,name='mdetails'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),


    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name='Demoapp//resetpass.html'),name='reset_password'),
    
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='Demoapp//resetsuccess.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='Demoapp//Passwordreset.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='Demoapp//Passwordconfirm.html'),name='password_reset_complete'),


    path('dummy/',views.dummy,name='dummy'),
    path('search/', views.search, name="search"),
    path('mlmodel/', views.mlmodel, name="mlmodel"),
    path('check/', views.check, name="check"),
    
]