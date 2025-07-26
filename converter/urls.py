# converter/urls.py (Правильна версія)

from django.urls import path
from . import views

app_name = 'converter'

urlpatterns = [
    path('', views.document_upload_view, name='document_upload'),

    path('status/<int:pk>/', views.check_document_status_view, name='check_document_status'),
]