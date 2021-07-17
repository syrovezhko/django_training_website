from django.contrib import admin
from .models import PriceCard, PriceTable

# Register your models here.

# price's table correction
class PriceAdmin(admin.ModelAdmin):
	list_display    = ('pc_title', 'pc_old_price', 'pc_new_price')
	list_editable   = ('pc_old_price', 'pc_new_price')
	readonly_fields = ('pc_title',)

# offer's cards correction
class CardAdmin(admin.ModelAdmin):
	list_display    = ('id', 'pc_value', 'pc_discription')
	list_editable   = ('pc_value', 'pc_discription')




admin.site.register(PriceCard, CardAdmin)
admin.site.register(PriceTable, PriceAdmin)