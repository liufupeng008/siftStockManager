from django.db import models
# Create your models here.
'''股票信息'''
class StockInfo(models.Model):

        # 股票交易所
        sexchange = models.CharField(max_length=10)

        # 公司名称
        scode = models.CharField(max_length=40)

        # 公司名称
        scompany_name = models.CharField(max_length=40)

        # 行业
        sindustry = models.CharField(max_length=40)

        # pe（扣非）
        spe_ttm = models.FloatField(max_length=40)

        # pb（不含商誉）
        spb = models.FloatField(max_length=40)

        # 股息率%
        sdividend_yield = models.FloatField(max_length=40)

        # 股价
        sstock_prices = models.FloatField(max_length=40)

        # pb（不含商誉）分为点10年
        spb_ten_year = models.FloatField(max_length=40)

        spe_sort = models.IntegerField(default=1)

        spb_sort = models.IntegerField(default=1)

        sdividend_yield_sort = models.IntegerField(default=1)

        synthetical_sort = models.IntegerField(default=1)

        def prn_obj(self):
            print('\n'.join(['%s:%s' % item for item in self.__dict__.items()]) )
