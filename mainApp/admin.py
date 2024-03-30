from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group
#
# @admin.register(Muallif)
# class MuallifAdmin(admin.ModelAdmin):
#     list_display = ('id', 'ism', 'jins', 't_sana', 'kitob_soni', 'tirik')
#     list_editable = ('tirik', 'kitob_soni')
#     list_display_links = ('id', 'ism')
#     search_fields = ('ism', 'id', 't_sana')
#     search_help_text = "Id, ism va sanasi orqali qidirish mumkin "
#     list_filter = ('tirik', 'jins')
#     ordering = ('ism', 't_sana', )
#     date_hierarchy = 't_sana'
#     list_per_page = 10

admin.site.register(Talaba)
# admin.site.register(Muallif)
# admin.site.register(Kitob)
@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'janr', 'sahifa', 'muallif',)
    list_editable = ('sahifa', )
    # list_display_links = ('id', 'ism')
    search_fields = ('nom', 'janr',)
    autocomplete_fields = ('muallif', )
class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ('ism', 'ish_vaqti')
    search_fields = ['ism']

admin.site.register(Kutubxonachi, KutubxonachiAdmin)

class MuallifAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'jins', 't_sana', 'kitob_soni', 'tirik')
    search_fields = ['ism']
    list_display_links = ('id', 'ism')
    list_editable = ('kitob_soni', 'tirik')

admin.site.register(Muallif, MuallifAdmin)

class RecordAdmin(admin.ModelAdmin):
    search_fields = ['talaba__ism', 'kitob__nom', 'kutubxonachi__ism']

admin.site.register(Record, RecordAdmin)

class UstozAdmin(admin.ModelAdmin):
    search_fields = ['ism']

admin.site.register(Ustoz, UstozAdmin)

class UniversitetAdmin(admin.ModelAdmin):
    search_fields = ['nom']

admin.site.register(Universitet, UniversitetAdmin)

class YonalishAdmin(admin.ModelAdmin):
    list_display = ('nom', 'aktiv')
    search_fields = ['nom']
    list_filter = ('aktiv',)

admin.site.register(Yonalish, YonalishAdmin)

class FanAdmin(admin.ModelAdmin):
    search_fields = ['nom']
    list_filter = ('asosiy', 'yonalish')

admin.site.register(Fan, FanAdmin)




admin.site.unregister(User)
admin.site.unregister(Group)
