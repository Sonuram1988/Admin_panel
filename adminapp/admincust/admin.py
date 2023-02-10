from django.contrib import admin
from .models import Image,Category

# Register your models here.

class custAdmin(admin.ModelAdmin):
    list_display=('title','description')
    list_editable=('description',)
    search_fields=('title',)

class imageAdmin(admin.ModelAdmin):
    list_display=('title','description','added_date','image')
    list_editable=('description','image')
    search_fields=('title',)
    list_per_page=2
    list_filter=('title',)








admin.site.register(Image,imageAdmin)
admin.site.register(Category,custAdmin)


