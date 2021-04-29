from django.contrib import admin
from .models import Video,AdminLogin,Movie,Review,Check
# Register your models here.
admin.site.register(Video)
admin.site.register(AdminLogin)
admin.site.register(Review)


class MovieAdmin(admin.ModelAdmin):
    list_display = ("movieId", "title", "genres", "imdbId", "average","description","image","video")
    search_fields = ['title']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Check)



