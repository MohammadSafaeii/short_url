from .models import ShortUrlUsage, ShortUrlUsageLastDay, ShortUrlUsageLastWeek, ShortUrlUsageLastMonth
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from django.template import loader
from django.http import HttpResponse
from api.models import urlHashmap


def calculate_parameters(item, filtered_data):
	shorturl = item['shorturl']
	general_count = item['count']
	device = {}
	device_per_user = {}
	browser = {}
	browser_per_user = {}
	shorturl_records = filtered_data.filter(shorturl=shorturl)
	csrf_token_grouped_data = shorturl_records.values('csrf_token').annotate(count=Count('id'))
	general_count_per_user = 0
	for item_csrf_token in csrf_token_grouped_data:
		if item_csrf_token['csrf_token'] == 'anonymous':
			general_count_per_user += item_csrf_token['count']
		else:
			general_count_per_user += 1
	device_grouped_data = shorturl_records.values('device').annotate(count=Count('id'))
	for item_device in device_grouped_data:
		device[item_device['device']] = item_device['count']
		shorturl_device_records = filtered_data.filter(shorturl=shorturl, device=item_device['device'])
		device_csrf_grouped_data = shorturl_device_records.values('csrf_token').annotate(count=Count('id'))
		device_per_user[item_device['device']] = 0
		for item_device_csrf_token in device_csrf_grouped_data:
			if item_device_csrf_token['csrf_token'] == 'anonymous':
				device_per_user[item_device['device']] += item_device_csrf_token['count']
			else:
				device_per_user[item_device['device']] += 1
	browser_grouped_data = shorturl_records.values('browser').annotate(count=Count('id'))
	for item_browser in browser_grouped_data:
		browser[item_browser['browser']] = item_browser['count']
		shorturl_browser_records = filtered_data.filter(shorturl=shorturl, browser=item_browser['browser'])
		browser_csrf_grouped_data = shorturl_browser_records.values('csrf_token').annotate(count=Count('id'))
		browser_per_user[item_browser['browser']] = 0
		for item_browser_csrf_token in browser_csrf_grouped_data:
			if item_browser_csrf_token['csrf_token'] == 'anonymous':
				browser_per_user[item_browser['browser']] += item_browser_csrf_token['count']
			else:
				browser_per_user[item_browser['browser']] += 1
	return shorturl, general_count, general_count_per_user, device, device_per_user, browser, browser_per_user


def create_url_used_records(start_time, end_time, short_url_usage_model):
	# yesterday = timezone.now() - timedelta(days=1)
	filtered_data = ShortUrlUsage.objects.filter(date_create__gt=start_time, date_create__lt=end_time)
	grouped_data = filtered_data.values('shorturl').annotate(count=Count('id'))
	for item in grouped_data:
		shorturl, general_count, general_count_per_user, device, device_per_user, browser, browser_per_user = calculate_parameters(item, filtered_data)
		short_url_usage_model.objects.create(
			shorturl=shorturl,
			general_count=general_count,
			general_count_per_user=general_count_per_user,
			device_count=device,
			device_count_per_user=device_per_user,
			browser_count=browser,
			browser_count_per_user=browser_per_user,
		)


def cronFillUrlUsageTable():
	end_time = timezone.localtime(timezone.now()).replace(hour=0, minute=0, second=0, microsecond=0)
	ShortUrlUsageLastDay.objects.all().delete()
	create_url_used_records((timezone.localtime(timezone.now()) - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0), end_time, ShortUrlUsageLastDay)
	ShortUrlUsageLastWeek.objects.all().delete()
	create_url_used_records((timezone.localtime(timezone.now()) - timedelta(days=7)).replace(hour=0, minute=0, second=0, microsecond=0), end_time, ShortUrlUsageLastWeek)
	ShortUrlUsageLastMonth.objects.all().delete()
	create_url_used_records((timezone.localtime(timezone.now()) - timedelta(days=30)).replace(hour=0, minute=0, second=0, microsecond=0), end_time, ShortUrlUsageLastMonth)


def userUrlData(request):
	if request.user.is_anonymous:
		template = loader.get_template("api/main_page.html")
		context = {
		}
		return HttpResponse(template.render(context, request))
	user_url_hashmaps = urlHashmap.objects.filter(user=request.user)
	response = {}
	start_time = timezone.localtime(timezone.now()).replace(hour=0, minute=0, second=0, microsecond=0)
	end_time = timezone.localtime(timezone.now())
	for item in user_url_hashmaps:
		filtered_data = ShortUrlUsage.objects.filter(date_create__gt=start_time, date_create__lt=end_time, shorturl=item.shorturl)
		try:
			grouped_data = filtered_data.values('shorturl').annotate(count=Count('id'))[0]
			shorturl, general_count, general_count_per_user, device, device_per_user, browser, browser_per_user = calculate_parameters(grouped_data, filtered_data)
		except:
			shorturl = general_count = general_count_per_user = device = device_per_user = browser = browser_per_user = 'NY'
		last_day_record = ShortUrlUsageLastDay.objects.filter(shorturl=item.shorturl).first()
		last_week_record = ShortUrlUsageLastWeek.objects.filter(shorturl=item.shorturl).first()
		last_month_record = ShortUrlUsageLastMonth.objects.filter(shorturl=item.shorturl).first()
		response.update({
			item.shorturl: {
				'general_count_today': general_count,
				'general_count_per_user_today': general_count_per_user,
				'devise_count_today': device,
				'devise_count_per_user_today': device_per_user,
				'browser_count_today': browser,
				'browser_count_per_user_today': browser_per_user,
				'general_count_last_day': last_day_record.general_count if last_day_record else 'NY',
				'general_count_per_user_last_day': last_day_record.general_count_per_user if last_day_record else 'NY',
				'devise_count_last_day': last_day_record.device_count if last_day_record else 'NY',
				'devise_count_per_user_last_day': last_day_record.device_count if last_day_record else 'NY',
				'browser_count_last_day': last_day_record.browser_count if last_day_record else 'NY',
				'browser_count_per_user_last_day': last_day_record.browser_count_per_user if last_day_record else 'NY',
				'general_count_last_week': last_week_record.general_count if last_week_record else 'NY',
				'general_count_per_user_last_week': last_week_record.general_count_per_user if last_week_record else 'NY',
				'devise_count_last_week': last_week_record.device_count if last_week_record else 'NY',
				'devise_count_per_user_last_week': last_week_record.device_count if last_week_record else 'NY',
				'browser_count_last_week': last_week_record.browser_count if last_week_record else 'NY',
				'browser_count_per_user_last_week': last_week_record.browser_count_per_user if last_week_record else 'NY',
				'general_count_last_month': last_month_record.general_count if last_month_record else 'NY',
				'general_count_per_user_last_month': last_month_record.general_count_per_user if last_month_record else 'NY',
				'devise_count_last_month': last_month_record.device_count if last_month_record else 'NY',
				'devise_count_per_user_last_month': last_month_record.device_count if last_month_record else 'NY',
				'browser_count_last_month': last_month_record.browser_count if last_month_record else 'NY',
				'browser_count_per_user_last_month': last_month_record.browser_count_per_user if last_month_record else 'NY'}
		})
	template = loader.get_template("analytics/user_url_data.html")
	return HttpResponse(template.render({'context': response}, request))
