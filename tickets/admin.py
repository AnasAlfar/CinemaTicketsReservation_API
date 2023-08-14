from django.contrib import admin
from .models import Guest,Movie,Reservation
from .models import Post

admin.site.register(Movie)
admin.site.register(Reservation)
admin.site.register(Guest)
admin.site.register(Post)