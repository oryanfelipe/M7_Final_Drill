from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto
from django.utils.html import format_html
from django.utils.safestring import mark_safe

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'checkbox')
    list_display_links = ('id', 'nombre')
    search_fields = ('nombre',)

    actions = ['add_selected_to_tickets']

    def checkbox(self, obj):
        return mark_safe('<input type="checkbox" name="selected" value="{}" />'.format(obj.pk))
    
    checkbox.short_description = ''
    
    def add_selected_to_tickets(self, request, queryset):
        # Implement the logic to add selected labs to tickets here
        pass

    add_selected_to_tickets.short_description = 'ADD LABORATORIO +'
    
@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'laboratorio')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')


admin.site.site_header = 'Django administration'
admin.site.index_title = 'Home'
admin.site.site_title = 'Laboratorio'