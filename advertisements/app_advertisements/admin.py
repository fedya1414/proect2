from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction',
                    'created_at', 'created_date', 'updated_date', 'image','get_html_image']
    list_filter = ['auction', 'created_at']


    actions = ['make_auction_as_false', 'make_auction_as_true']




    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    fieldsets = (
        ('Общее',{
            'fields':('title', 'description', 'image'),
        }),
        ('Финансы',{
            'fields':('price','auction'),
            'classes':['collapse']
        })
    )



admin.site.register(Advertisement,AdvertisementAdmin)

# Register your models here.
