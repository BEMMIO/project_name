from django.urls import path
from . import views

app_name = 'page'

urlpatterns = [
    path('', views.page_view,name='page-view'),
    path('about/', views.page_view2,name='page-view-about'),

]
