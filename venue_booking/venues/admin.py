from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Venue)
admin.site.register(Booking)