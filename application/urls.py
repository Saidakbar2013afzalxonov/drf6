# from django.urls import path
# from . import views

# urlpatterns = [
#     path("employees/", views.EmployeeListAPIView.as_view(), name="employees-list"),
#     path("employees/create/", views.EmployeeCreateAPIView.as_view(), name="employees-create"),
#     path("employees/<int:pk>/", views.EmployeeRetrieveAPIView.as_view(), name="employees-detail"),
#     path("employees/<int:pk>/update/", views.EmployeeUpdateAPIView.as_view(), name="employees-update"),
#     path("employees/<int:pk>/delete/", views.EmployeeDestroyAPIView.as_view(), name="employees-delete"),
#     path("employees/list-create/", views.EmployeeListCreateAPIView.as_view(), name="employees-list-create"),
#     path("employees/<int:pk>/retrieve-update/", views.EmployeeRetrieveUpdateAPIView.as_view(), name="employees-retrieve-update"),
#     path("employees/<int:pk>/retrieve-destroy/", views.EmployeeRetrieveDestroyAPIView.as_view(), name="employees-retrieve-destroy"),
#     path("employees/<int:pk>/retrieve-update-destroy/",views.EmployeeRetrieveUpdateDestroyAPIView.as_view(),name="employees-retrieve-update-destroy"),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeList, name='employee-list'),
    path('employee/<int:pk>/', views.EmployeeView, name='employee-view'),
    path('employee/create/', views.EmployeeCreate, name='employee-create'),
    path('employee/update/<int:pk>/', views.EmployeeUpdate, name='employee-update'),
    path('employee/delete/<int:pk>/', views.EmployeeDelete, name='employee-delete'),

    path('employees-list-create/', views.EmployeeListCreate, name='employee-list-create'),
    path('employee-detail/<int:pk>/', views.EmployeeDetail, name='employee-detail'),
]
