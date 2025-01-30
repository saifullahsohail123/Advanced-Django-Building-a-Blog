from django.contrib import admin

# Register your models here.

from blog.models import Tag, Post



class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


# Here we’re setting just one attribute, prepopulated_fields. When used in this way, some JavaScript is inserted into the admin page so that 
# the slug field updates when the title field changes. It will automatically “slugify” the title.


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)

# Now that the PostAdmin class is defined, let’s return to the register function. The PostAdmin class is passed as the second argument: