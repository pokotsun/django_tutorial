from django.contrib import admin

# Register your models here.
from .models import Choice, Question

# class QuestionAdmin(admin.ModelAdmin):
# Adminページで表示するカラムの順番を変える
    # fields = ['pub_date', 'question_text']

# Adminページで各カラムをグループ化して表示する
#    fieldsets = [
#        (None,               {'fields': ['question_text']}),
#        ('Date information', {'fields': ['pub_date']}),
#    ]

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1 

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] # pub_dateでfilterをかけられるようにする
    search_fields = ['question_text'] # question_fieldで検索できるようにする

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

