from django.urls import path
from Todo_List import views

urlpatterns = [
    path('',views.todo, name= 'todo'),
    path('task_views', views.task_views, name = 'task_views'),
    path('update/<int:id>', views.Update, name="todo_update"),
    path('delete/<int:id>', views.Delete, name="todo_delete"),
    path('search',views.search,name='search'),
]
