from .models import Course, Instructors, Category, Exam, Certificate
from modeltranslation.translator import TranslationOptions, register


@register(Course)
class ProductTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')


@register(Instructors)
class ProductTranslationOptions(TranslationOptions):
    fields = ('full_name', 'instructor_bio')


@register(Category)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Exam)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'passing_score', 'duration')


@register(Certificate)
class ProductTranslationOptions(TranslationOptions):
    fields = ('students', 'course', 'issued_at',)
