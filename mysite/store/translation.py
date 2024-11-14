from .models import Hotel
from modeltranslation.translator import TranslationOptions,register


@register(Hotel)
class TranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'description')
