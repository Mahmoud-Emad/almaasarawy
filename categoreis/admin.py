from django.contrib import admin
from categoreis.models import MotherCategory,Category,SubCategory,SubMultiCategory

admin.site.register(MotherCategory)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SubMultiCategory)


