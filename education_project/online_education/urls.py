from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'user_profiles', UserProfileViewSet, basename='user_list')
router.register(r'instructors', InstructorsViewSet, basename='instructors_list')
router.register(r'students', StudentsViewSet, basename='students_list')
router.register(r'categories', CategoryViewSet, basename='categories_list')
router.register(r'carts', CartViewSet, basename='carts_list')
router.register(r'car_items', CarItemViewSet, basename='car_items_list')
router.register(r'lessons', LessonViewSet, basename='lessons_list')
router.register(r'assignments', AssignmentViewSet, basename='assignments')
router.register(r'questions', QuestionViewSet, basename='questions_list')
router.register(r'exams', ExamViewSet, basename='exams_list')
router.register(r'certificates', CertificateViewSet, basename='certificates_list')
router.register(r'reviews', ReviewViewSet, basename='reviews_list')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', include(router.urls)),
    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),

]

