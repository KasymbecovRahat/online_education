from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    USER_CHOICES = (
        ('проподаватель', 'проподаватель'),
        ('студент', 'студент')
    )
    user_role = models.CharField(max_length=32, choices=USER_CHOICES, default='студент')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Instructors(models.Model):
    full_name = models.CharField(max_length=50)
    instructor_bio = models.TextField()
    instructor_image = models.ImageField(upload_to='teacher_image/')


class Students(models.Model):
    full_name = models.CharField(max_length=50)
    students_bio = models.TextField()
    students_image = models.ImageField(upload_to='students_image/')


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_name


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    LEVEL_CHOICES = (
        ('начальный', 'начальный'),
        ('средний', 'средний'),
        ('продвинутый', 'продвинутый')
    )
    level = models.CharField(max_length=16, choices=LEVEL_CHOICES, default='начальный')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(Instructors, on_delete=models.CASCADE, related_name='created_by_course')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=32)
    video_url = models.FileField(upload_to='lesson_video/')
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')


class Assignment(models.Model):
    title = models.CharField(max_length=32)
    title_description = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    students = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='students_assignments')


class Question(models.Model):
    question_name = models.TextField()

    def __str__(self):
        return self.question_name


class Exam(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exams')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_exams')
    passing_score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 101)], verbose_name='Баллы')
    duration = models.DateTimeField(null=True, blank=True)


class Certificate(models.Model):
    students = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='certificate')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_certificate')
    issued_at = models.DateTimeField(null=True, blank=True)
    certificate_url = models.FileField()


class Review(models.Model):
    user = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='review_user')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='review_course')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')
    comment = models.TextField()




