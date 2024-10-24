from django.contrib import admin

# Register your models here.
from api import models as api_model

admin.site.register(api_model.User)
admin.site.register(api_model.Profile)
admin.site.register(api_model.Post)
admin.site.register(api_model.Gallery)
admin.site.register(api_model.Quote)