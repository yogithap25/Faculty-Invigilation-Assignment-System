from django.contrib import admin

# Register your models here.
from .models import ExamSession
from .models import Assignment
from .models import Feedback

admin.site.register(ExamSession)
admin.site.register(Assignment)
admin.site.register(Feedback)