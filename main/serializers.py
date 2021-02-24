from rest_framework import serializers, validators
from .models import Customer
from datetime import date
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class CustomerSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    user = UserSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'

    @staticmethod
    def get_age(obj):
        today = date.today()
        age = today.year - obj.date_of_birth.year - (
                (today.month, today.day) < (obj.date_of_birth.month, obj.date_of_birth.day)
        )
        return age

    def create(self, validated_data):
        if self.context.get('user', None) is None:
            raise validators.ValidationError({'message': 'user auth not provided'})
        customer = Customer.objects.create(user=self.context['user'], **validated_data)
        return customer
