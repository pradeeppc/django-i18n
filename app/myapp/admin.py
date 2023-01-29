from django.contrib import admin
from myapp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'translation']


admin.site.register(Article, ArticleAdmin)
