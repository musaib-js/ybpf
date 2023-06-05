from django.contrib import admin
from .models import Event, EventImages, Member, Blog, Query

class EventImageAdmin(admin.StackedInline):
    model = EventImages

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageAdmin]

    class Meta:
        model = Event

@admin.register(EventImages)
class EventImageAdmin(admin.ModelAdmin):
    pass

admin.site.register((Member, Blog, Query))