from rest_framework import serializers
from user_authentication.models import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['user', 'title', 'description', 'price',
                  'author', 'publish_date', 'visibility']
