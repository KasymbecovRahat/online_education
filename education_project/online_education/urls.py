from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserProfileViewSet, InstructorsViewSet, StudentsViewSet, CategoryViewSet,
    CourseViewSet, CartViewSet, CarItemViewSet, LessonViewSet, AssignmentViewSet,
    QuestionViewSet, ExamViewSet, CertificateViewSet, ReviewViewSet
)

router = DefaultRouter()
router.register(r'user_profiles', UserProfileViewSet, basename='user_list')
router.register(r'instructors', InstructorsViewSet, basename='instructors_list')
router.register(r'students', StudentsViewSet, basename='students_list')
router.register(r'categories', CategoryViewSet, basename='categories_list')
router.register(r'courses', CourseViewSet, basename='courses_list')
router.register(r'carts', CartViewSet)
router.register(r'car_items', CarItemViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
