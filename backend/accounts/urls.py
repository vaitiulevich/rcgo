from django.urls import path
from .views import user, password_reset, password_change, add_info, info

urlpatterns = [
    path('user/', user),
    path('user/reset_password/', password_reset),
    path('user/change_password/', password_change),
    path('user/add_info/<int:pk>', add_info),
    path('user/info/', info)
]
