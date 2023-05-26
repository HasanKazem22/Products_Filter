from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Categories)
admin.site.register(Brands)
admin.site.register(Warranty)
admin.site.register(Filter_Price)
admin.site.register(Product)