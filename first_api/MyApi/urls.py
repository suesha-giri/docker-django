from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns=[
    path('api',views.ApiView.as_view(), name='api'),
    path('count',views.CountView.as_view(), name='count'),
    path('dbList',views.DblistView.as_view(), name='dbList'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
   
]