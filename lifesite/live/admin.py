from django.contrib import admin
from . models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title_text']}),
        ('Admin body', {'fields': ['body']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = []

    list_display = ('title_text', 'body', 'pub_date')
    list_display_links = ['title_text']
    search_fields = ['title']


"""
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]   # This include Choices in the Questions from admin.site

    list_display = ('question_text', 'pub_date', 'was_published_recently')    #This show the question of a good presentation
    list_filter = ['pub_date']
    search_fields = ['question_text']
"""

admin.site.register(Article, ArticleAdmin)

