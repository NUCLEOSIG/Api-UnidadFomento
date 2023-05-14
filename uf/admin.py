from django.contrib import admin
from uf.models import UnidaddeFomento


@admin.register(UnidaddeFomento)
class UFAdmin(admin.ModelAdmin):
    pass
