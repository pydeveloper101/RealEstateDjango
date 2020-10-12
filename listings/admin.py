from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','price','list_date','realtor','is_published')
    list_display_links = ('id','title')
    list_filter = ('id','title','price','list_date','realtor','is_published')
    list_editable = ('is_published',)
    search_fields = ('title','description')
    list_per_page = 25

admin.site.register(Listing,ListingAdmin)

# Register your models here.
