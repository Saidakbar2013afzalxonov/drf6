from django.urls import path
from . import views

urlpatterns = [
    path("employees/", views.EmployeeListAPIView.as_view()),
    path("employee/<int:pk>/", views.EmployeeRetrieveAPIView.as_view()),
    path("employee/create/", views.EmployeeCreateAPIView.as_view()),
    path("employee/update/<int:pk>/", views.EmployeeUpdateAPIView.as_view()),
    path("employee/delete/<int:pk>/", views.EmployeeDestroyAPIView.as_view()),

    path("employees2/", views.EmployeeListCreateAPIView.as_view()),
    path("employee/ru/<int:pk>/", views.EmployeeRetrieveUpdateAPIView.as_view()),
    path("employee/rd/<int:pk>/", views.EmployeeRetrieveDestroyAPIView.as_view()),
    path("employee/rud/<int:pk>/", views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),
]