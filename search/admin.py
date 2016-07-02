from django.contrib import admin

# Register your models here.
from .models import Search
from .models import Site

class SearchAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "query"]
	class Meta:
		model = Search

class SiteAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "url"]
	class Meta:
		model = Site

admin.site.register(Search, SearchAdmin)
admin.site.register(Site, SiteAdmin)