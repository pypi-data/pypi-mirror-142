from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from localflavor.generic.models import IBANField, BICField


class SEPAMandate(models.Model):
    """A SEPA direct debit mandate."""

    payment = models.OneToOneField(settings.PAYMENT_MODEL, on_delete=models.CASCADE, related_name="sepa_mandate")
    
    account_holder = models.CharField(verbose_name=_("Account holder"), max_length=64)
    iban = IBANField(verbose_name=_("IBAN of bank account"))
    bic = BICField(verbose_name=_("BIC/SWIFT code of bank"))

    date = models.DateField(verbose_name=_("Date mandate was granted"), auto_now_add=True)
