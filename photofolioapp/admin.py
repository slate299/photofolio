from django.contrib import admin
from .models import ContactMessage, Photo

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')  # Customize the fields displayed in the list view
    list_filter = ('created_at',)  # Add filters by date
    search_fields = ('name', 'email', 'subject', 'message')  # Add a search bar
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')  # Make fields read-only

# Alternatively, you can register without the decorator:
# admin.site.register(ContactMessage, ContactMessageAdmin)
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'category')
    list_filter = ('category',)