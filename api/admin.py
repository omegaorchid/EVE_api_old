from django.contrib import admin

# Register your models here.
from .models import Join


#  Admin page customisation
class JoinAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'first_name', 'timestamp', 'updated']

    class Meta:
        model = Join

admin.site.register(Join, JoinAdmin)
