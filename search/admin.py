from django.contrib import admin

# Register your models here.
from .models import Search
from .models import Site
from .models import Result

class SearchAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "site"]
	class Meta:
		model = Search

class SiteAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "url"]
	class Meta:
		model = Site
		
class ResultAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "url"]
	class Meta:
		model = Result

admin.site.register(Search, SearchAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Result, ResultAdmin)