from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from .models import User
from .models import Student


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # for any additional fields you'd like to add to the JWT sent back in response
        # add below using the token["field name"] = user.name_of_property
        # token["is_student"] = user.is_student

        token["username"] = user.username
        token["first_name"] = user.first_name
        token["is_student"] = user.is_student
        token["is_teacher"] = user.is_teacher
        token["is_active"] = user.is_active

        return token


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = ('username', 'password', 'email',
                  'first_name', 'last_name', 'is_student', 'is_teacher', 'is_active'
                  )
        class Meta:
            model = Student
            fields = ('qr_id', 'points_balance')
                # see below * - should Student fields be separate?

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_student=validated_data['is_student'],
            is_teacher=validated_data['is_teacher'],
            is_active=validated_data['is_active'],
            
        student = Student.objects.create( 
            qr_id=validated_data['qr_id'],
            points_balance=validated_data['points_balance'])
            # see below * - should Student fields be separate?

            #///
            # If added new columns through the User model, add them in this
            # create method. Example below:
            # is_student=validated_data['is_student']
            #///
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

# //// * Student User fields??
        # student= Student.objects.create(
        #     qr_id=validated_data['qr_id'],
        #     points_bank=validated_data['points_bank'],
        #     shopping_cart=validated_data['shopping_cart']
        # )
        # student.save()
        # return student