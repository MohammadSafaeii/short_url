from django.contrib import admin
from .models import ShortUrlUsage, ShortUrlUsageLastDay, ShortUrlUsageLastWeek, ShortUrlUsageLastMonth


class ShortUrlUsageAdmin(admin.ModelAdmin):
	list_display = ['shorturl', 'csrf_token', 'device', 'browser', 'date_create']
	search_fields = ['shorturl', 'csrf_token', 'device', 'browser', 'date_create']


class ShortUrlUsageLastDayAdmin(admin.ModelAdmin):
	list_display = ['shorturl', 'general_count', 'general_count_per_user', 'device_count', 'device_count_per_user', 'browser_count', 'browser_count_per_user']
	search_fields = ['shorturl', 'general_count', 'general_count_per_user', 'device_count', 'device_count_per_user', 'browser_count', 'browser_count_per_user']


class ShortUrlUsageLastWeekAdmin(admin.ModelAdmin):
	list_display = ['shorturl', 'general_count', 'general_count_per_user', 'device_count', 'device_count_per_user', 'browser_count', 'browser_count_per_user']
	search_fields = ['shorturl', 'general_count', 'general_count_per_user', 'device_count', 'device_count_per_user', 'browser_count', 'browser_count_per_user']


class ShortUrlUsageLastMonthAdmin(admin.ModelAdmin):
	list_display = ['shorturl', 'general_count', 'general_count_per_user', 'device_count', 'device_count_per_user', 'browser_count', 'browser_count_per_user']
	search_fields = ['shorturl', 'general_count', 'general_count_per_user', 'device_count', 'device_count_per_user', 'browser_count', 'browser_count_per_user']


# Register the model with the admin site
admin.site.register(ShortUrlUsage, ShortUrlUsageAdmin)
admin.site.register(ShortUrlUsageLastDay, ShortUrlUsageLastDayAdmin)
admin.site.register(ShortUrlUsageLastWeek, ShortUrlUsageLastWeekAdmin)
admin.site.register(ShortUrlUsageLastMonth, ShortUrlUsageLastMonthAdmin)
