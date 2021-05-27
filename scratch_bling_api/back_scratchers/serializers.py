from rest_framework import serializers

class SizeSerializer(serializers.Serializer):
        size = serializers.CharField(max_length=10)


class BackScratchersSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=30)
    size = SizeSerializer(many=True)

