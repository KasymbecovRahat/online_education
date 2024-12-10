from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name',
                  'last_name', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class InstructorsSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    total_people = serializers.SerializerMethodField()

    class Meta:
        model = Instructors
        fields = ['full_name', 'avg_rating', 'total_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_total_people(self, obj):
        return obj.get_total_people()


class InstructorsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructors
        fields = ['full_name', 'instructor_bio', 'instructor_image']


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarItem
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['']


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    course = InstructorsSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    total_people = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['course_name', 'course_image', 'instructorS',
                  'price', 'avg_rating', 'total_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_total_people(self, obj):
        return obj.get_total_people()


class CourseDetailSerializer(serializers.ModelSerializer):
    course = InstructorsDetailSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    total_people = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['course_name', 'description', 'category', 'level',
                  'price', 'created_by', 'created_at', 'update_at', 'course_image', 'course',
                  'avg_rating', 'total_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_total_people(self, obj):
        return obj.get_total_people()
