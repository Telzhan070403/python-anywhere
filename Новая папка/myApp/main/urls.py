from django.contrib.auth.views import LoginView
from django.urls import path
from .import views
from .views import logout_user, RegisterUser, EmailAttachementView

urlpatterns = [
    path('', views.home),
    path('sut/', views.sut),
    path('flour/', views.flour),
    path('sports/', views.sports),
    path('winter/', views.winter),
    path('summer/', views.summer),
    path('news/', views.news),
    path('mens/', views.mens),
    path('womens/', views.womens),
    path('boots/', views.boots),
    path('insert/', views.insert),
    # path('send/', views.sendMail),
    # path('registration_done/', views.register_done, name='register_done'),
    path('send/', EmailAttachementView.as_view(), name='emailattachment'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
]
