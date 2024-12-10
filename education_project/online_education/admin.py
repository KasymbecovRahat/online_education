from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


class AssignmentInLine(admin.TabularInline):
    model = Assignment
    extra = 1



class LessonAdmin(admin.ModelAdmin):
    inlines = [AssignmentInLine]





@admin.register(Course)
class CourseAdmin(TranslationAdmin):

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
admin.site.register(Exam)
admin.site.register(Certificate)
admin.site.register(Review)

