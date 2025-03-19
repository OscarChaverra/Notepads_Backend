from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='sign_up'),
    path('login/', views.Login.as_view(), name='login'),
<<<<<<< Updated upstream
=======
    path('google-login/', views.GoogleLoginView.as_view(),name='google-login'),
>>>>>>> Stashed changes
    path('my-profile/',views.myProfile.as_view(), name="myProfile"),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
