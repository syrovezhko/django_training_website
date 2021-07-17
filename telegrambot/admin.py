from django.contrib import admin
from .models        import TelegramSettings

# Register your models here.
class TelegramQuickSet(admin.ModelAdmin):
	list_display       = ('id', 'tg_name', 'tg_user_name', 'tg_message')
	list_display_links = ('id', 'tg_name', 'tg_user_name')
	list_editable      = ('tg_message',)

admin.site.register(TelegramSettings, TelegramQuickSet)