 
from django.urls import path
from DemoApp import views

urlpatterns = [
path('gm/', views.gm_view),
path('ga/', views.ga_view),
path('ge/', views.ge_view),

path('student/<int:id>/', views.student_detail),

]