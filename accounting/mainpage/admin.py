from django.contrib import admin
from .models import Department, Division, Sector, CustomUser, UserSectorAccess, UserDivisionAccess

admin.site.register(Department)
admin.site.register(Division)
admin.site.register(Sector)
admin.site.register(UserSectorAccess)
admin.site.register(UserDivisionAccess)
