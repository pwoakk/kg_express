from django.contrib import admin

from backend.apps.order.models import Order, OrderItem


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product',]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'address',
        'postal_code',
        'mobile',
        'created',
        'status',
    ]
    list_filter = [
        'status',
        'created',
    ]
    search_fields = [
        'address',
        'user__email',
        'mobile',
        'id',
    ]
    readonly_fields = [
        'user',
        'address',
        'postal_code',
        'mobile',
        'notice',
    ]
    inlines = [OrderItemInLine]
