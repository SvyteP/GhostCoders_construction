
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.classify_title, name='classify_title'),
    # path('download_output/', views.download_output, name='download_output'),

    # path('', views.index, name='index'),
    path('classify/', views.classify_title, name='classify_title'),
    path('upload/', views.upload_file, name='upload_file'),
    path('download/', views.download_output, name='download_output'),
]
