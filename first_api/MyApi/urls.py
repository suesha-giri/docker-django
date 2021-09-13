from django.urls import path
from . import views

urlpatterns=[
    path('api',views.api, name='api'),
    path('count',views.count, name='count'),
    path('dblist',views.dbList, name='dbList')
]