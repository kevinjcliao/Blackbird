from django.contrib import admin
from blog.models import *


"""
class TitleAdmin(admin.ModelAdmin): 
    fieldsets = [
            (None,              {'fields': ['title_text']}), 
            ('Publishing Date', {'fields': ['pub_date'], 'classes': ['collapse']}), 
    ]
    inlines = [Post_Content_In_Line]
    
"""

class Blog_Post_Admin(admin.ModelAdmin): 
    fieldsets = [
            (None,              {'fields': ['title_text']}), 
            ('Publishing Date', {'fields': ['pub_date'], 'classes': ['collapse']}),
            ('Post Content',    {'fields': ['post_content_text']}), 
        ]

admin.site.register(Blog_Post, Blog_Post_Admin)
