from django.contrib import admin
from .models import Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip', 'subject', 'send_on')
    list_filter = ['send_on']
    search_fields = ['name', 'subject']

admin.site.register(Message, MessageAdmin)