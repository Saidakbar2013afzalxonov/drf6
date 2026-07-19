# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Employee
# from .serializers import EmployeeSerializer
# from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView


# # Create your views here.

# class EmployeeListAPIView(ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer



# class EmployeeRetrieveAPIView(RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer



# class EmployeeCreateAPIView(CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer



# class EmployeeUpdateAPIView(UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer



# class EmployeeDestroyAPIView(DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer



# class EmployeeListCreateAPIView(ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer



# class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializer


@api_view(['GET'])
def EmployeeList(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def EmployeeView(request, pk):
    employee = Employee.objects.get(pk=pk)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)


@api_view(['POST'])
def EmployeeCreate(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(
        {"message": "Ma'lumotlar noto'g'ri kiritildi!"},
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['PUT', 'PATCH'])
def EmployeeUpdate(request, pk):
    employee = Employee.objects.get(pk=pk)

    serializer = EmployeeSerializer(employee, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(
        {"message": "Xodimni yangilashda xatolik yuz berdi!"},
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['DELETE'])
def EmployeeDelete(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()

    return Response(
        {"message": "Xodim o'chirildi!"},
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET', 'POST'])
def EmployeeListCreate(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            {"message": "Ma'lumotlar noto'g'ri kiritildi!"},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def EmployeeDetail(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            {"message": "Xodimni to'liq yangilashda xatolik yuz berdi!"},
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'PATCH':
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            {"message": "Xodimni qisman yangilashda xatolik yuz berdi!"},
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        employee.delete()
        return Response(
            {"message": "Xodim muvaffaqiyatli o'chirildi!"},
            status=status.HTTP_204_NO_CONTENT
        )