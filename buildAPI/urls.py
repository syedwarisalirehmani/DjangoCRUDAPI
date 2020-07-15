from django.urls import path
from buildAPI import views

urlpatterns = [
    path('user/register', views.userCreate, name='create_user'),
    path('user/test', views.getDemo, name='test_user'),
    path('user/userList', views.getUser, name='user_list'),
    path('user/userList/<str:id>/', views.detailUser, name='detail_user'),
    path('user/user_update/<str:id>/', views.userUpdate, name='update_user'),
    path('user/delete_user/<str:id>/', views.deleteUser, name='delete_user')
]