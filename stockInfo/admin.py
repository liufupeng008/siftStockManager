from django.contrib import admin
from stockInfo.models import StockInfo

# Register your models here.
@admin.register(StockInfo)
class stockInfoAdmin(admin.ModelAdmin):
        list_display = ['sexchange', 'scode','scompany_name','sindustry',
                        'spe_ttm','spb','sdividend_yield','sstock_prices','spb_ten_year',
                        'spe_sort','spb_sort','sdividend_yield_sort','synthetical_sort']

