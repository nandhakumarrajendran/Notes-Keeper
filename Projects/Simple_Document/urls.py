from django.urls import path
from . import views

urlpatterns = [
    path('',views.Create_Document,  name = 'create_document'),
    path('view_document/',views.View_Document,  name = 'view_document'),
    path('delete/<int:id>',views.Delete, name= 'delete_document'),
    path('update/<int:id>',views.Update, name= 'update_document'),
    path('search',views.search,name='search'),
]
