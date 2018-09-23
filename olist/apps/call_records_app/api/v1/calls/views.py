from rest_framework import generics

from .serializers import CallRecordSerializer


class CreateCallRecordView(generics.CreateAPIView):
    """
    post:
     Create a new Call record instance.
    """
    serializer_class = CallRecordSerializer
