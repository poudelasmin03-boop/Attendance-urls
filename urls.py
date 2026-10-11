from django.urls import path

from .views import (
    home_views,
    register_new_student,
    verify_student,
    dashboard_views,
    attendance_views,
    verify_face,
    attendance_history,
)

urlpatterns = [
    path("", home_views, name="home"),
    path("register_new_student", register_new_student, name="register_new_student"),
    path("verify_student/", verify_student, name="verify_student"),
    path("verify_face/", verify_face, name="verify_face"),
    path("dashboard/", dashboard_views, name="dashboard"),
    path("attendance_views/", attendance_views, name="attendance_views"),
    path("attendance_history/", attendance_history, name="attendance_history"),
]
