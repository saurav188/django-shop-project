from django.urls import path
from user import views

urlpatterns = [
    path('login/',views.login,name="login_page"),
    path('logout',views.logout,name="logout_page"),
    path('user_info/',views.user_info,name="user_info"),
    path('edituserinfo/',views.edituserinfo,name="edit_user_info"),
    path('changepassword/',views.change_password,name="change_password"),
    path('register/',views.register,name="register_page"),
]