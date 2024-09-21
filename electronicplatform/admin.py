from django.contrib import admin
# from django.utils.html import format_html
# from django.urls import reverse

from .models import PlatformUnit, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Отображение продукта в панели администратора"""
    list_display = (
        "id",
        "name",
        "model",
        "release_date",
        "network_unit",
    )
    list_filter = ("network_unit",)
    search_fields = ("name",)
    list_display_links = ("name", "network_unit")


@admin.register(PlatformUnit)
class PlatformUnitAdmin(admin.ModelAdmin):
    """Отображение модели единицы платформы в панели администратора"""
    list_display = (
        "id",
        "name",
        "country",
        "city",
        "type",
        "level",
        "supplier",
        "debt",
        "date_create",
        "email",
        )
    list_filter = ("city",)
    search_fields = ("name",)
    actions = ("clear_debt",)
    list_display_links = ("name", "supplier",)

    # def trader_link(self, obj):
    #     """Ссылка для перехода в карточку трейдера"""
    #     if obj.supplier:
    #         url = reverse('admin:electronicplatform_supplier_change', args=[obj.supplier.id])
    #         return format_html('<a href="{}">{}</a>', url, obj.supplier)
    #     return '-'
    # trader_link.short_description = 'Трейдер'
    # def supplier_link(self, obj):
    #     if obj.supplier:
    #         url = f"admin/electronicplatform/supplier/{obj.supplier.id}/change/"
    #         # Прописываем url ссылки на поставщика
    #         return format_html(f'<a href="{url}">{obj.supplier.name}</a>')
    #     return 'Поставщик не указан'
    # supplier_link.short_description = 'Поcтавщик'

    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(modeladmin, request, queryset):
        """Действие удаления задолженности"""
        queryset.update(debt=0.00)
