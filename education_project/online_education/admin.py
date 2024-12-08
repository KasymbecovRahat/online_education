from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *

class CategoryInLine(admin.TabularInline):
    model = Category
    extra = 1

class AssignmentInLine(admin.TabularInline):
    model = Assignment
    extra = 1

class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 1

class LessonAdmin(admin.ModelAdmin):
    inlines = [AssignmentInLine]

class ExamAdmin(admin.ModelAdmin):
    inlines = [QuestionInLine]



@admin.register(Course)
class HotelAdmin(TranslationAdmin):
    inlines = [CategoryInLine]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
admin.site.register(Instructors)
admin.site.register(Students)
admin.site.register(Cart)
admin.site.register(CarItem)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Certificate)
admin.site.register(Review)
