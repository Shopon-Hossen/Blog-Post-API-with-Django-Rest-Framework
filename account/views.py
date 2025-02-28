from rest_framework.response import Response
from rest_framework.views import APIView
from account.models import User
from blog.models import Blog
from account.utils import get_token_for_user
from rest_framework import status
from blog.serializer import BlogListSerializer
from account.serializer import (
    UserSerializer,
    UserDetailSerializer
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            tokens = get_token_for_user(user)
            return Response({'user': serializer.data, 'tokens': tokens}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(password):
            return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)

        tokens = get_token_for_user(user)
        return Response({'tokens': tokens}, status=status.HTTP_200_OK)


class GetUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateUserView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        data = request.data.copy()
        if 'email' in data or 'password' in data:
            return Response({'error': 'Email or Password update is not allowed'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(request.user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        if not request.user.check_password(old_password):
            return Response({'error': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)

        request.user.set_password(new_password)
        request.user.save()
        return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)


class ProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'


class UserBlogListView(ListAPIView):
    serializer_class = BlogListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Blog.objects.filter(author=pk)
