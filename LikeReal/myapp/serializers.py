from rest_framework import serializers
from .models import person



class personserializer(serializers.ModelSerializer):
    class Meta:
        model = person
        fields = ("username","fullname","email","phone","password","confirmpassword",)

    def create(self, validated_data):
        return person.objects.create(**validated_data)