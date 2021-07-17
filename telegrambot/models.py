from django.db import models

# Create your models here.
class TelegramSettings(models.Model):
	tg_name      = models.CharField(max_length     = 200, null = True, default = '-',
								verbose_name   = 'Имя бота')
	tg_user_name = models.CharField(max_length     = 200, null = True, default = '-', 
								verbose_name   = 'Telegram id бота')
	tg_token     = models.CharField(max_length     = 200,
								verbose_name   = 'Токен')
	tg_chat      = models.CharField(max_length     = 200,
								verbose_name   = 'Чат id')
	tg_message   = models.TextField(verbose_name = 'Текст сообщения')

	def __str__(self):
		return self.tg_name


	class Meta:
		verbose_name        = 'настройку'
		verbose_name_plural = 'Настройки'
