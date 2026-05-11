from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),  # Make admin login the default page
    path('dashboard/', views.dashboard, name='dashboard'),
    path('assignments/', views.assignments, name='assignments'),
    path('history/', views.assignment_history, name='history'),
    path('logout/', views.logout_view, name='logout'),
    path('test-data/', views.test_data, name='test_data'),
    path('upload/', views.upload, name='upload'),
    path('assignment-search/', views.assignment_search, name='assignment_search'),
    path('manage-exams/', views.manage_exam_sessions, name='manage_exam_sessions'),
    path('tag-assignments/', views.tag_assignments_to_exam, name='tag_assignments_to_exam'),
    path('send-assignment-notifications/', views.send_assignment_notifications, name='send_assignment_notifications'),
    path('feedback/', views.feedback_view, name='feedback'),
    # Add more paths as you build more views
]