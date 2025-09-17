from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Poll, Option
from .serializers import PollSerializer

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    @action(detail=True, methods=["post"])
    def vote(self, request, pk=None):
        option_id = request.data.get("option_id")
        try:
            option = Option.objects.get(id=option_id, poll_id=pk)
            option.votes += 1
            option.save()
            return Response({"message": "Vote counted!"})
        except Option.DoesNotExist:
            return Response({"error": "Invalid option"}, status=400)
