from django.contrib import admin

# we need to import something that we want to show up in the blog app
from blogapp.models import Post

admin.site.register(Post)