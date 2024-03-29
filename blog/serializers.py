from rest_framework import serializers
from .models import Exponant, ExponantComment
from django.urls import reverse

class ExponantCommentSerializer(serializers.ModelSerializer):
    exponant = serializers.StringRelatedField(read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = ExponantComment
        fields = "__all__"
class ExponantSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Exponant
        fields = ('id','title', 'subtitle', 'img')
    def get_comment(self, obj):
        comments = ExponantComment.objects.filter(blog=obj)[:-3]
        request = self.context.get('request')
        return {
            "comments": ExponantCommentSerializer(comments, many=True).data,
            "all_comment_link": request.build_absolute_uri(reverse('exponant_list', kwargs={'exponant_id': obj.id}))
        }

