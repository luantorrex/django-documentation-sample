from dataclasses import fields
from django.contrib import admin

from .models import Choice, Question

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    
    # Objetos “Choice são editados na mesma página de administração de Question.
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
