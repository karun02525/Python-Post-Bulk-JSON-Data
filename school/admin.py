from django.contrib import admin
from .models import ExamCenter,Student,Teacher

# Register your models here.

@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname','city']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','roll','cname','city']

@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','age','city']

