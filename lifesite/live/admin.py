from django.contrib import admin
from . models import Article, Blog

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['blog']}),
        ('Admin body', {'fields': ['body']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = []

    list_display = ('blog', 'body', 'pub_date')
    list_display_links = ['blog']
    search_fields = ['blog']


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

admin.site.register(Article)

