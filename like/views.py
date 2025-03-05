from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from like.models import Like
from like.serializers import LikeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status



class LikeCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        post_id = request.data.get('post')
        if not post_id:
            return Response(
                {"detail": "Post id not provided"},
                status=status.HTTP_400_BAD_REQUEST
            )
        like = Like.objects.filter(user=user, post=post_id).first()
        if not like:
            return Response(
                {"detail": "Like not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        like.delete()
        return Response(
            {"detail": "Unlike successfully"},
            status=status.HTTP_200_OK
        )