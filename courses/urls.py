from django.urls import path
from courses import views


urlpatterns = [
    path('', views.CoursesList.as_view(), name="courses"),
    path('<slug:username>/<slug:year>/<slug:month>/<slug:slug>/', views.CourseDetail.as_view(), name='course_detail'),   
]