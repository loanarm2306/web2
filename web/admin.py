from django.contrib import admin

# This is how you can register your models with the Django admin so that you can manage them from the admin interface

from .models import Passengers, DeparturePoint, ArrivalPoint, DepartureTime, ArrivalTime, Distance, TransportId, TransportType

admin.site.register(TransportType)
admin.site.register(TransportId)
admin.site.register(Passengers)
admin.site.register(DeparturePoint)
admin.site.register(ArrivalPoint)
admin.site.register(DepartureTime)
admin.site.register(ArrivalTime)
admin.site.register(Distance)
