from django.contrib import admin
from .models import Category, Ranking, Product
from mptt.admin import MPTTModelAdmin


class CategoryAdmin(MPTTModelAdmin):
    """
    Category admin model
    """
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name',]
    raw_id_fields = ("author",)


class RankingAdmin(admin.ModelAdmin):
    """
    Ranking admin model
    """
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', ]
    raw_id_fields = ("category","author")


class ProductAdmin(admin.ModelAdmin):
    """
    Product admin model
    """
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title',]
    raw_id_fields = ("ranking","author")


admin.site.register(Ranking, RankingAdmin)
admin.site.register(Category , CategoryAdmin)
admin.site.register(Product , ProductAdmin)

