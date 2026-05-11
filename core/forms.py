from django import forms
from .models import ExamSession, Feedback, Assignment

class AssignmentSearchForm(forms.Form):
    exam_type = forms.ChoiceField(
        choices=[('', 'All')] + ExamSession.EXAM_TYPE_CHOICES,
        required=False,
        label="Exam Type",
    )
    date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
    )


class ExamSessionForm(forms.ModelForm):
    class Meta:
        model = ExamSession
        fields = ['name', 'exam_type', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.RadioSelect(choices=Feedback.RATING_CHOICES),
            'comment': forms.Textarea(
                attrs={'placeholder': 'Tell us what is on your mind...', 'rows': 3}
            ),
        }