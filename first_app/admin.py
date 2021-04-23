from django.contrib import admin
from first_app.models import contactus
from first_app.models import hospital
from first_app.models import experts
from first_app.models import consult
from first_app.models import appointment
# Register your models here.
admin.site.register(contactus)
admin.site.register(hospital)
admin.site.register(experts)
admin.site.register(consult)
admin.site.register(appointment)
