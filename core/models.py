from django.db import models
from django.utils import timezone

# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    availability = models.TextField(blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)  # Added email field

    def __str__(self):
        return f"{self.name}"

class Room(models.Model):
    room_number = models.CharField(max_length=20)
    strength = models.IntegerField()
    block = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.room_number

class ExamSession(models.Model):
    EXAM_TYPE_CHOICES = [
        ('midterm', 'Midterm'),
        ('semester_end', 'Semester End'),
        # Add more as needed
    ]
    name = models.CharField(max_length=100)  # e.g., "Midterm March 2024"
    exam_type = models.CharField(
        max_length=20, 
        choices=EXAM_TYPE_CHOICES,
        default='midterm',
        blank=True,
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_exam_type_display()} ({self.name})"

class Assignment(models.Model):
    ROLE_CHOICES = [
        ('invigilator', 'Invigilator'),
        ('floor', 'Floor Incharge'),
        ('attendance', 'Attendance Incharge'),
    ]
    exam_session = models.ForeignKey(
        ExamSession,
        on_delete=models.CASCADE,
        related_name='assignments',
        null=True,
        blank=True,
    )
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    invigilator = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        related_name='invigilations',
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='invigilator')

    class Meta:
        ordering = ['date', 'room__room_number']

    def __str__(self):
        return f"{self.date} - {self.room} - {self.invigilator} ({self.role})"

class Feedback(models.Model):
    RATING_CHOICES = [
        ('great', 'Great'),
        ('indifferent', 'Indifferent'),
        ('unhappy', 'Unhappy'),
    ]
    rating = models.CharField(max_length=12, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.rating} - {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"
