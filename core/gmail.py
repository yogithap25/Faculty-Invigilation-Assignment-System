from core.models import Assignment
Assignment.objects.filter(exam_session__isnull=True).delete()
exit()