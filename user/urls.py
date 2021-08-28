from django.urls import path

from user.views import UserListView, user_create, user_update, user_delete


urlpatterns = [
    path('', UserListView.as_view(), name="users_list"),
    path('create/', user_create, name="users_create"),
    path('update/<int:pk>/', user_update, name="update_user"),
    path('delete/<int:pk>/', user_delete, name="delete_user"),
]
