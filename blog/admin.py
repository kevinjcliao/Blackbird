from django.contrib import admin
from blog.models import *


class Blog_Post_Admin(admin.ModelAdmin): 
    fieldsets = [
            (None,              {'fields': ['title_text']}), 
            ('Publishing Date', {'fields': ['pub_date'], 'classes': ['collapse']}),
            ('Cover Image',     {'fields': ['post_photo']}), 
            ('Post Content',    {'fields': ['post_content_text']}), 
        ]

admin.site.register(Blog_Post, Blog_Post_Admin)
