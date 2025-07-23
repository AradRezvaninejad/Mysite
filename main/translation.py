from modeltranslation.translator import register, TranslationOptions
from .models import Profile, PortfolioItem, Certificate, PortfolioProject

@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'description', 'location')

@register(PortfolioItem)
class PortfolioItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Certificate)
class CertificateTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(PortfolioProject)
class PortfolioProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'category')
