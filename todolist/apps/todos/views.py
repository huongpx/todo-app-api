from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import generics

from .models import Todos
from .serializers import TodosSerializer


class TodosList(generics.ListCreateAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
    @extend_schema(
        summary="Lấy danh sách tất cả todo",
        responses={
            201: OpenApiResponse(response=TodosSerializer,
                                 description='Success'),
            400: OpenApiResponse(description='Lỗi lấy danh sách todo'),
        },
    )
    def get(self, request, *args, **kwargs):
        """ 
        API tạo todo mới
        """
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        summary="Tạo todo mới",
        responses={
            201: OpenApiResponse(response=TodosSerializer,
                                 description='Đã tạo todo mới'),
            400: OpenApiResponse(description='Lỗi tạo todo'),
        },
    )
    def post(self, request, *args, **kwargs):
        """ 
        API tạo todo mới
        """
        return super().post(request, *args, **kwargs)
    
    
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
    
    @extend_schema(
        summary="lấy thông tin todo bằng id",
        responses={
            201: OpenApiResponse(response=TodosSerializer,
                                 description='Success'),
            400: OpenApiResponse(description='Lỗi lấy todo'),
        },
    )
    def get(self, request, *args, **kwargs):
        """ 
        API lấy thông tin todo bằng id
        """
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        summary="Update todo",
        responses={
            201: OpenApiResponse(response=TodosSerializer,
                                 description='Đã cập nhật todo'),
            400: OpenApiResponse(description='Lỗi cập nhật todo'),
        },
    )
    def put(self, request, *args, **kwargs):
        """ 
        API update todo mới
        """
        return super().put(request, *args, **kwargs)
    
    @extend_schema(
        summary="Xóa todo",
        responses={
            201: OpenApiResponse(response=TodosSerializer,
                                 description='Đã xóa todo'),
            400: OpenApiResponse(description='Lỗi xóa todo'),
        },
    )
    def delete(self, request, *args, **kwargs):
        """ 
        Xóa todo
        """
        return super().delete(request, *args, **kwargs)
    
    
