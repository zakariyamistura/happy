from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "user","title","created_at",]
    list_filter = ["created_at", "user"]
    search_fields = ["tittle", "created_at"]
    readonly_fields = ["id", "created_at"]


admin.site.register(Blog, BlogAdmin)