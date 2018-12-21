from django.contrib import admin
from df_user.models import Career,College,University,UserInfo
# Register your models here.
admin.site.register(College)
admin.site.register(Career)
admin.site.register(University)
admin.site.register(UserInfo)