from django.urls import path
from taskapp import views
from taskapp.views import TaskListView, TaskCreateView, TaskPreviousListView, TaskDetailView, \
    ChecklistCreateView, ChecklistUpdateView, ChecklistDeleteView, TaskDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.index, name="index"),
    path('', TaskListView.as_view(), name="index"),
    path('task/', TaskCreateView.as_view(), name="create-task"),
    path('previous/', TaskPreviousListView.as_view(), name="previous"),
    path('task/<int:task_id>/', TaskDetailView.as_view(), name="view-task"),
    path('task/<int:task_id>/item/', ChecklistCreateView.as_view(), name="create-item"),
    path('task/<int:task_id>/item/<int:check_id>/', ChecklistUpdateView.as_view(), name="check-item"),

    path('task/<int:task_id>/delete/', TaskDeleteView.as_view(), name="delete-task"),
    path('task/<int:task_id>/item/<int:check_id>/delete/', ChecklistDeleteView.as_view(), name="delete-item"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
