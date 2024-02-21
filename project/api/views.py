from rest_framework.viewsets import mixins, GenericViewSet
from api.models import Task
from api.serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404


class TaskViewSet(mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):

    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()

    def list(self, request, *args, **kwargs):
         serializer = self.serializer_class(self.get_queryset(), many=True)
         return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Task, pk=pk)
        serializer = self.serializer_class(instance, request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Task, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
