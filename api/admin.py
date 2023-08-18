from django.contrib import admin
from .models import UrlHashmap


class urlHashmapAdmin(admin.ModelAdmin):
	list_display = ['longurl', 'shorturl', 'user']
	search_fields = ['longurl', 'shorturl' 'user']


# Register the model with the admin site
admin.site.register(UrlHashmap, urlHashmapAdmin)
