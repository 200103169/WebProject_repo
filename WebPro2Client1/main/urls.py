from django.urls import path
from .import views

urlpatterns = [

    path('upload/', views.model_form_upload),
    path('insert/', views.insert),
    path('', views.news, name='news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('login', views.loginPage, name='login'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
]
