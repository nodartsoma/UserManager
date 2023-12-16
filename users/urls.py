from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_users, name="list of users"),
    path('create/', views.create_users, name="create users"),
    path('delete/<int:pk>', views.delete_users, name="delete users"),
]
