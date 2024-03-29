from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import serializers
from .models import Exponant, ExponantComment
from .serializers import ExponantSerializer, ExponantCommentSerializer
from rest_framework import generics
from functools import reduce
import operator
from django.db.models import Q
from rest_framework import viewsets, mixins
# Create your views here.

class ExponantListApi(generics.ListAPIView):
    queryset = Exponant.objects.all()
    serializer_class = ExponantSerializer

class ExponantDetailApiView(generics.RetrieveAPIView):
    queryset = Exponant.objects.all()
    serializer_class = ExponantSerializer

class ExponantDeleteApiView(generics.DestroyAPIView):
    queryset = Exponant.objects.all()
    serializer_class = ExponantSerializer
class ExponantUpdateApiView(generics.UpdateAPIView):
    queryset = Exponant.objects.all()
    serializer_class = ExponantSerializer
class ExponantCreateApiView(generics.CreateAPIView):
    queryset = Exponant.objects.all()
    serializer_class = ExponantSerializer
class ExponantUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exponant.objects.all()
    serializer_class = ExponantSerializer

class ExponantSearchViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Exponant.objects.all()
    serializer_class = ExponantSerializer

    def get_queryset(self):
        text = self.request.query_params.get('query', None)
        if not text:
            return self.queryset
        text_seq = text.split(' ')
        text_qs = reduce(operator.and_,
                         (Q(title__icontains=i) for i in text_seq))
        return self.queryset.filter(text_qs)

class ExponantCommentListCreateView(generics.ListCreateAPIView):
    queryset = ExponantComment.objects.all()
    serializer_class = ExponantCommentSerializer

    def get_queryset(self):
        exponant_id = self.kwargs.get('exponant_id')
        return ExponantComment.objects.filter(exponant_id=exponant_id)
    def perform_create(self, serializer):
        exponant_id = self.kwargs.get('exponant_id')
        exponant = get_object_or_404(Exponant, id=exponant_id)
        if ExponantComment.objects.filter(exponant=exponant, author=self.request.user).exists():
            raise serializers.ValidationError({'Message': 'Siz allaqachon kamment yozgansiz'})
        serializer.save(author=self.request.user, exponant=exponant)







