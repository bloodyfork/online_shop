from rest_framework.generics import DestroyAPIView

class DeleteAddress(DestroyAPIView):
    serializer_class =