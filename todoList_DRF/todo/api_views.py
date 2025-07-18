from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status, generics, filters
from rest_framework import viewsets
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .pagination import CustomPageNumberPagination


class TodoListAPI(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data) # 일반 json데이터 .data


class TodoCreateAPI(APIView):
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)


class TodoRetrieveAPI(APIView):
    def get(self, requeset, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"error": "해당 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    

class TodoUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def patch(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)


class TodoDeleteAPI(APIView):
    def delete(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

# DRF_GenericAPIView
# list
class TodoGenericsListAPI(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# create
class TodoGenericsCreateAPI(generics.CreateAPIView):
    serializer_class = TodoSerializer


# retrieve
class TodoGenericsRetrieveAPI(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# update
class TodoGenericsUpdateAPI(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# destroy
class TodoGenericsDestoryAPI(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# ListCreate
class TodoGenericsListCreateAPI(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# RetrieveUpdateDestroy
class TodoGenericsRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# DRF_ViewSets
# viewSet
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    # pagination
    pagination_class = CustomPageNumberPagination

    # 인증
    authentication_classes = [SessionAuthentication]

    # 권한
    permission_classes = [IsAuthenticated]

    # 이미지
    parser_classes = [MultiPartParser, FormParser]

    # 검색기능
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "description"]

    def get_queryset(self):
        qs = Todo.objects.all().order_by("-created_at")
        return qs


# LogoutAPI
class CustomLogoutAPI(APIView):
    def get(self, request):
        logout(request)
        return redirect('todo:todo_List')
        # return Response({"message": "로그아웃 완료"}, status=status.HTTP_200_OK)
