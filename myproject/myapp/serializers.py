from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length = 250)
    author = serializers.CharField(max_length = 250)
    published_date = serializers.DateField()