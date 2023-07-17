from django.urls import  path
from .views import *
urlpatterns = [
    path('',Test),
    path('post/',Test_post),
    path('<int:pk>/',PostDetail.as_view()),
    path('hom/',PostList.as_view())
    
]

