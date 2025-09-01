from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('new/', views.note_form, name='note_form'),
    path('note/new/', views.note_create, name='note_create'),
    path('tag/<str:tag>/', views.tag_search, name='tag_search'),
    path('search/', views.search_by_tag, name='search_by_tag'),
    path('notes/<int:pk>/delete/', views.delete_note, name='delete_note'),
]