from about_us.models import Person, Role
from django.contrib import admin


class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_filter = ('first_name',)
    search_fields = ['first_name', 'last_name']


admin.site.register(Person, PersonAdmin)
admin.site.register(Role)