from django.contrib import admin
from myapp.models import Article
# Register your models here.

# admin.site.register(Article)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'translation']


admin.site.register(Article, ArticleAdmin)
