from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from quotes.serializers import QuoteSerializer
from quotes.models import Quote


class QuoteListApiView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = QuoteSerializer(Quote.objects.all(), many=True)
        return Response(serializer.data)   

    def post(self, request):
        serializer = QuoteSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'errors': serializer.errors})
        
        newQuote = Quote()
        newQuote.author = serializer.validated_data['author']
        newQuote.quote = serializer.validated_data['quote']
        newQuote.save()
        return Response(serializer.data)   

    


class QuoteApiView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        serializer = QuoteSerializer(Quote.objects.get(id=pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = QuoteSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'errors': serializer.errors})
        
        quote = get_object_or_404(Quote, id=pk)
        quote.author = serializer.validated_data['author']
        quote.quote = serializer.validated_data['quote']
        quote.save()
        return Response(serializer.data) 

    def delete(self, request, pk):
        quote = get_object_or_404(Quote, id=pk)
        quote.delete()
        return Response({})   

