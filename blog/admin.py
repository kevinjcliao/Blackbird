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
admin.site.register(Blog_Post)
