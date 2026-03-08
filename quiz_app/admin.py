from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question, Choice, QuizResult, UserAnswer

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(QuizResult)
admin.site.register(UserAnswer)