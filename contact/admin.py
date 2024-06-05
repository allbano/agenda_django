from django.contrib import admin

from contact import models


# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name",] 
    ordering = ["name",]
    search_fields = ["id","name",]
    list_per_page = 20
    list_max_show_all = 100
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["id","first_name", "last_name","show", "phone", "email", "created_date",] 
    ordering = ["first_name",]
    search_fields = ["id","first_name", "last_name", "email",]
    list_per_page = 20
    list_max_show_all = 100
    list_editable = ["first_name", "last_name","show",]
    list_display_links = ["id","phone"]