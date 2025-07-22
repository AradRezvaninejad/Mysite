from django.db import models
from django.utils.translation import gettext_lazy as _
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Profile(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    title = models.CharField(_("Title"), max_length=150)
    description = models.TextField(_("Description"))
    photo = models.ImageField(_("Photo"), upload_to="profiles/", blank=True, null=True)

    age = models.PositiveIntegerField(_("Age"), blank=True, null=True)
    location = models.CharField(_("Location"), max_length=100, blank=True, null=True)
    email = models.EmailField(_("Email"), blank=True, null=True)
    phone = models.CharField(_("Phone"), max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    profile = models.ForeignKey(Profile, related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(_("Skill Name"), max_length=50)
    proficiency = models.PositiveSmallIntegerField(_("Proficiency %"))  # 0 to 100

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"

class PortfolioItem(models.Model):
    profile = models.ForeignKey(Profile, related_name="portfolio_items", on_delete=models.CASCADE)
    title = models.CharField(_("Project Title"), max_length=100)
    description = models.TextField(_("Project Description"))
    image = models.ImageField(_("Project Image"), upload_to="portfolio/", blank=True, null=True)

    def __str__(self):
        return self.title
    

class Certificate(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    issue_date = models.DateField(_("Issue Date"))
    description = models.TextField(_("Description"), blank=True)
    image = models.ImageField(_("Certificate Image"), upload_to='certificates/')
    url = models.URLField(_("Verification URL"), blank=True)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='certificates'
    )

    class Meta:
        ordering = ['-issue_date']
        verbose_name = _("Certificate")
        verbose_name_plural = _("Certificates")

    def __str__(self):
        return f"{self.title}"
    

class PortfolioProject(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Project Title"))
    description = models.TextField(verbose_name=_("Project Description"))
    category = models.CharField(max_length=100, verbose_name=_("Category"), blank=True)
    image = models.ImageField(upload_to='portfolio/', verbose_name=_("Project Image"), blank=True, null=True)
    link = models.URLField(blank=True, null=True, verbose_name=_("Project Link"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Portfolio Project")
        verbose_name_plural = _("Portfolio Projects")
        ordering = ['-created_at']

    def __str__(self):
        return self.title