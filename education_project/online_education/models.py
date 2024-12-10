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
    user_picture = models.ImageField(upload_to='user_picture/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Instructors(models.Model):
    full_name = models.CharField(max_length=50)
    instructor_bio = models.TextField()
    instructor_image = models.ImageField(upload_to='teacher_image/')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='instructor')

    def __str__(self):
        return f'{self.full_name} {self.instructor_bio} {self.user_profile}'

    def get_avg_rating(self):
        ratings = self.instructors_review.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0


class Students(models.Model):
    full_name = models.CharField(max_length=50)
    students_bio = models.TextField()
    students_image = models.ImageField(upload_to='students_image/')
    user_profiles = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return f'{self.full_name} {self.students_bio} {self.user_profiles}'


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
    instructorS = models.ForeignKey(Instructors, on_delete=models.CASCADE, related_name='course')
    course_image = models.ImageField(upload_to='course_image/')

    def __str__(self):
        return f'{self.course_name} {self.price} {self.category}'

    def get_avg_rating(self):
        ratings = self.review_course.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0

    def get_total_people(self):
        ratings = self.review_course.all()
        if ratings.exists():
            return ratings.count()
        return 0


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='cart')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())


class CarItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def get_total_price(self):
        return self.course.price * self.quantity


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=32)
    video_url = models.FileField(upload_to='lesson_video/')
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return f'{self.lesson_name} {self.course} {self.content}'


class Assignment(models.Model):
    title = models.CharField(max_length=32)
    title_description = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    students = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='students_assignments')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_assignment')

    def __str__(self):
        return f'{self.title} {self.course} {self.lesson}'


class Exam(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exams')
    passing_score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 101)], verbose_name='Баллы')
    duration = models.DateTimeField(null=True, blank=True)
    students = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='students_exam')
    instructors = models.ForeignKey(Instructors, on_delete=models.CASCADE, related_name='instructors_exam')

    def __str__(self):
        return f'{self.title} {self.course} {self.passing_score}'


class Question(models.Model):
    question_name = models.CharField(max_length=100)
    var1 = models.CharField(max_length=55)
    var2 = models.CharField(max_length=55)
    var3 = models.CharField(max_length=55)
    var4 = models.CharField(max_length=55)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.question_name


class Certificate(models.Model):
    students = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='certificate')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_certificate')
    issued_at = models.DateTimeField(null=True, blank=True)
    certificate_url = models.FileField()

    def __str__(self):
        return f'{self.certificate_url}, {self.course}'


class Review(models.Model):
    user = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='review_user')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='review_course')
    instructor = models.ForeignKey(Instructors, on_delete=models.CASCADE, related_name='instructors_review')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')
    comment = models.TextField()

    def __str__(self):
        return f'{self.user} {self.course} {self.rating}'




