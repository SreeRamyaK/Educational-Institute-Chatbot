from django.contrib import admin
from . models import custom_user,user_personal_model,staff_database
# Register your models here.
admin.site.register(custom_user)
admin.site.register(user_personal_model)
admin.site.register(staff_database)