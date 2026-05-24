from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    
    
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','category']
    list_filter = ['category']
    search_fields = ['name']
    list_per_page = 10


admin.site.register(Table)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    autocomplete_fields = ['food']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','total_price','status','payment_status']
    list_filter = ['status','payment_status']
    search_fields = ['user__username']
    list_per_page = 10
    inlines = [OrderItemInline]
admin.site.register(Order,OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id','order','food']
    list_filter = ['order']
    search_fields = ['food__name']
    list_per_page = 10
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Payment)
admin.site.register(Reservation)
