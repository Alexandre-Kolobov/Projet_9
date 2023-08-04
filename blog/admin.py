from django.contrib import admin
from . import models

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date_created')
    search_fields = ('title', 'user', 'date_created')

admin.site.register(models.Ticket, TicketAdmin)
