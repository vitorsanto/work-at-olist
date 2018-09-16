from rest_framework import generics

from .serializer import CallRecordSerializer


class CreateCallRecordView(generics.CreateAPIView):
    """
    post:
     Create a new Call record instance.
    """
    serializer_class = CallRecordSerializer
