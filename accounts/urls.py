from . import views
from django.urls import path
urlpatterns=[
  
    # username='superadmin',
    #email='superadmin@example.com',
    # password='superpassword'

    #username='alice',
    #email='alice@example.com',
    #password='1234',
    
    #username='john',
    #email='john@example.com',
    #password='1234'
    path('', views.login_view, name='login'),
    # Redirections possibles
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('user-dashboard/', views.user_dashboard_view, name='user_dashboard'),
]