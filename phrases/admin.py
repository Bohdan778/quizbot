from django.contrib import admin
from .models import Phrase


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    list_display = ("text", "translation", "is_fake")
    list_filter = ("is_fake",)
    search_fields = ("text", "translation")
