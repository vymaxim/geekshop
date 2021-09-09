from django.contrib import admin

from baskets.admin import BasketAdmin
from users.models import User

# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdmin,)