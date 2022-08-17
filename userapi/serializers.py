from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        # fields = ('id', 'firstname', 'lastname')

    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    #     instance.firstname = validated_data.get('firstname', instance.firstname)
    #     instance.lastname = validated_data.get('lastname', instance.lastname)
    #     instance.save()
    #     return instance
